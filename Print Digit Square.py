# Print Digit Square
# Given an integer N as the input, the program must print the square of each of the digits in N. If the digit is an odd digit then the square value is printed as a negative value.

# Boundary Condition(s):
# -999999999 <= N <= 999999999

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains all the square value of the digits of N as per the given conditions.

# Example Input/Output 1:

# Input:
# 1234

# Output:
# -14-916

# Example Input/Output 2:

# Input:
# 246

# Output:
# 41636






s = input().strip()
t=''
for i in s:
    if i=='-':
        t='-'
        continue
    i = int(t+i)
    if i%2:
        print(-(i*i),end='')
    else:
        print(i*i,end='')
    t=''