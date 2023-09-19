# Valid Octal Representation

# The program must accept an integer N as the input. The program must print YES if N is a valid octal representation. Else the program must print NO as the output.

# Boundary Condition(s):
# 1 <= N <= 10^7

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# 45

# Output:
# YES

# Explanation:
# The decimal equivalent of (45)8 is 37.
# So 45 is a valid octal representation.
# Hence the output is YES

# Example Input/Output 2:
# Input:
# 814

# Output:
# NO



# Max Execution Time Limit: 500 millisecs







i = input().strip()
try:
    int(i,8)
    print('YES')
except:
    print('NO')