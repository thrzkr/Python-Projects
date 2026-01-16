import pygame
import sys
import random

# --- Constants ---
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 133, 244)
RED = (219, 68, 55)
BG_COLOR = (240, 240, 240)
MENU_HEIGHT = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)


def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x*CELL_SIZE, MENU_HEIGHT),
                         (x*CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, MENU_HEIGHT + x*CELL_SIZE),
                         (WIDTH, MENU_HEIGHT + x*CELL_SIZE), LINE_WIDTH)


def draw_board(board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            center = (x*CELL_SIZE + CELL_SIZE//2,
                      MENU_HEIGHT + y*CELL_SIZE + CELL_SIZE//2)
            if board[y][x] == 'X':
                pygame.draw.line(
                    screen, RED, (center[0]-40, center[1]-40), (center[0]+40, center[1]+40), LINE_WIDTH)
                pygame.draw.line(
                    screen, RED, (center[0]+40, center[1]-40), (center[0]-40, center[1]+40), LINE_WIDTH)
            elif board[y][x] == 'O':
                pygame.draw.circle(screen, BLUE, center, 40, LINE_WIDTH)


def check_winner(board):
    lines = []
    lines.extend(board)  # rows
    lines.extend([[board[y][x] for y in range(GRID_SIZE)]
                 for x in range(GRID_SIZE)])  # columns
    lines.append([board[i][i] for i in range(GRID_SIZE)])  # diag
    lines.append([board[i][GRID_SIZE-1-i]
                 for i in range(GRID_SIZE)])  # anti-diag
    for line in lines:
        if line.count(line[0]) == GRID_SIZE and line[0] != '':
            return line[0]
    if all(board[y][x] != '' for y in range(GRID_SIZE) for x in range(GRID_SIZE)):
        return 'Draw'
    return None


def ai_move(board, ai_symbol):
    empties = [(y, x) for y in range(GRID_SIZE)
               for x in range(GRID_SIZE) if board[y][x] == '']
    if empties:
        y, x = random.choice(empties)
        board[y][x] = ai_symbol


def menu():
    while True:
        screen.fill(BG_COLOR)
        title = font.render("Tic Tac Toe", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        x_btn = small_font.render("Play as X (First)", True, WHITE)
        o_btn = small_font.render("Play as O (Second)", True, WHITE)
        x_rect = pygame.Rect(WIDTH//2 - 120, 120, 220, 50)
        o_rect = pygame.Rect(WIDTH//2 - 120, 190, 220, 50)
        pygame.draw.rect(screen, RED, x_rect)
        pygame.draw.rect(screen, BLUE, o_rect)
        screen.blit(x_btn, (x_rect.x + 20, x_rect.y + 10))
        screen.blit(o_btn, (o_rect.x + 20, o_rect.y + 10))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x_rect.collidepoint(event.pos):
                    return 'X'
                elif o_rect.collidepoint(event.pos):
                    return 'O'


def main():
    streak = 0
    while True:
        player_symbol = menu()
        ai_symbol = 'O' if player_symbol == 'X' else 'X'
        board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        turn = 'X'
        game_over = False
        winner = None
        streak_updated = False  # Ensure streak only updates once per game

        while True:
            screen.fill(BG_COLOR)
            pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, MENU_HEIGHT))
            draw_grid()
            draw_board(board)
            status = f"Turn: {turn}" if not game_over else (
                f"{winner} wins!" if winner != 'Draw' else "Draw!")
            status_surf = small_font.render(status, True, BLACK)
            screen.blit(status_surf, (20, 20))

            # Draw streak counter at the top right
            streak_text = f"Streak: {streak}"
            streak_surf = small_font.render(streak_text, True, BLACK)
            screen.blit(
                streak_surf, (WIDTH - streak_surf.get_width() - 20, 20))

            pygame.display.flip()

            if not game_over and turn == ai_symbol:
                pygame.time.wait(500)
                ai_move(board, ai_symbol)
                winner = check_winner(board)
                game_over = winner is not None
                turn = player_symbol
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not game_over and turn == player_symbol and event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if my > MENU_HEIGHT:
                        x, y = mx // CELL_SIZE, (my - MENU_HEIGHT) // CELL_SIZE
                        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and board[y][x] == '':
                            board[y][x] = player_symbol
                            winner = check_winner(board)
                            game_over = winner is not None
                            turn = ai_symbol

            if game_over and not streak_updated:
                if winner == player_symbol:
                    streak += 1
                elif winner == 'Draw':
                    pass
                else:
                    streak = 0
                streak_updated = True

            if game_over:
                msg = small_font.render(
                    "", True, BLACK)
                screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT - 60))
                pygame.display.flip()
                pygame.time.wait(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        break
                else:
                    continue
                break


if __name__ == "__main__":
    main()
