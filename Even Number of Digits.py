# Even Number of Digits
# Given an array of N integers, the program must print only the integers with even number of digits.

# Boundary Condition(s):
# 1 <= N <= 9999

# Input Format:
# The first line contains N.
# The next line contains N integers separated by space.

# Output Format:
# The first N line contains the specified output.

# Example Input/Output 1:
# Input:
# 5
# 12 345 15 1678 158

# Output:
# 12 15 1678

# Example Input/Output 2:
# Input:
# 7
# 1243 592 589 903 83403 1693 56

# Output:
# 1243 1693 56




input()
for i in input().split():
    if len(i)%2==0:
        print(i,end=' ')