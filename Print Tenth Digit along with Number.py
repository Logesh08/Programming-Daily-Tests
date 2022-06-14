# Print Tenth Digit along with Number
# Given a positive integer N where tenth digit is missing, the sum S of tenth digit T and unit digit U is provided. The program must print the number N along with the tenth digit included.

# Boundary Condition(s):
# 1 <= N <= 999999999999999
# 0 <= S <= 18
# U <= S <= T
# 0 <= T <= 9

# Input Format:
# The first line contains N.
# The second line contains Sum.

# Output Format:
# The first line contains number N along with the tenth digit T.

# Example Input/Output 1:

# Input:
# 1235
# 9

# Output:
# 12345

# Explanation:

# 9-5=4, 4 is tenth digit

# 12345 prints

# Example Input/Output 2:

# Input:
# 2468
# 15

# Output:
# 24678






n = input().strip()
s = int(input())
ans = s - int(n[-1])
print(n[:-1],ans,n[-1],sep='')