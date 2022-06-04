# Pattern Printing - Rotate
# Given a number N as input, the program must print the pattern as shown in the following examples.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first N lines contain the pattern as showned in the following example.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 1 2 3 4 5
# 5 1 2 3 4
# 4 5 1 2 3
# 3 4 5 1 2
# 2 3 4 5 1

# Example Input/Output 2:
# Input:
# 7

# Output:
# 1 2 3 4 5 6 7
# 7 1 2 3 4 5 6
# 6 7 1 2 3 4 5
# 5 6 7 1 2 3 4
# 4 5 6 7 1 2 3 
# 3 4 5 6 7 1 2
# 2 3 4 5 6 7 1













arr = [i for i in range(1,int(input())+1)]
for _ in range(len(arr)):
    print(*arr)
    arr = [arr[-1]]+arr[:-1]