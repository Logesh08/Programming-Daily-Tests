# Product of N and the Number of Digits
# Accept a number N as the input. The program must print the product of the number N and the number of digits in it as the output.

# Boundary Condition(s):
# 1 <= N <= 99999999

# Input Format:
# The first line contains the number N.

# Output Format:
# The first line contains the product of N and the number of digits in it.

# Example Input/Output 1:
# Input:
# 12

# Output:
# 24

# Explanation:
# Number of digits in 12 is 2 (1 and 2).
# So, 12 * 2 = 24.
# Thus, 24 is the output.

# Example Input/Output 2:
# Input:
# 19234

# Output:
# 96170

# Explanation:
# Number of digits in 19234 is 5 (1,9,2,3 and 4).
# So, 19234 * 5 = 96170.
# Thus, 96170 is the output.












s = input().strip()
print(len(s)*int(s))