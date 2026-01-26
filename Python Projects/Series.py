'''
Write code that accepts one input. The input represents the required number of terms for the following series.

an = 4 - 7n

if the input is less than or equal to zero, then print "Input must be more than zero" and do not run the loop.

for example, if the user enters 3, the program should calculate the first three terms in this sequence:

a1 = 4 - 7 * 1 = -3

a2 = 4 - 7 * 2 = -10

a3 = 4 - 7 * 3 = -17
'''
a1 = int(input())
d = int(input())

terms = []
for n in range(2, 12):
    an = a1 + (n - 1) * d
    terms.append(an)

print(", ".join(map(str, terms)), end=",")
