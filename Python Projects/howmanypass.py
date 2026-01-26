"""
A class contains 5 students. Write code that counts and 
print the number of students got mark more than or equal 
to 60. Use loop that runs 5 times and accept input each
time. Count all inputs that are more than or equal to 60.
Print the result as shown in the examples.
"""
pass_count = 0
for i in range(5):
    mark = float(input())
    if mark >= 60:
        pass_count += 1

print(f"{pass_count} students pass the course")
