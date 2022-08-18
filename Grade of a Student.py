# Grade of a Student

# The marks scored by a student is given as the input to the program. The program must print the corresponding grade based on the below conditions.

# Conditions:
# S Grade: 80 <= marks <= 100
# A Grade: 60 <= marks < 80
# B Grade: 50 <= marks < 60
# C Grade: marks < 50

# Example Input/Output 1:
# Input:
# 95

# Output:
# S

# Example Input/Output 2:
# Input:
# 34

# Output:
# C





mark = int(input())
print('S' if mark in range(80,100) else 'A' if mark in range(60,80) else 'B' if mark in range(50,60) else 'C')