# Integer Box Pattern

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 10^17

# Input Format:
# The first line contains N.

# Output Format:
# The first three lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 45

# Output:
# +--+
# |45|
# +--+

# Example Input/Output 2:
# Input:
# 12045

# Output:
# +-----+
# |12045|
# +-----+



# Max Execution Time Limit: 500 millisecs








n=input().strip()
l=len(n)
print('+'+'-'*l+'+','|'+n+'|','+'+'-'*l+'+',sep='\n')