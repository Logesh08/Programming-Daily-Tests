# Sum of Tenth Digits
# An array of N integers is passed as input. The program must print the sum of tenth digits of all the given integers.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the sum of all the tenth digits.

# Example Input/Output 1:
# Input:
# 4
# 410 50 320 610

# Output:
# 9

# Example Input/Output 2:
# Input:
# 5
# 56 23 140 150 84

# Output:
# 24










input() 
sum=0 
arr=input().split() 
for i in arr:
    if len(i)>1:
        sum+=(i[-2])
print(sum)