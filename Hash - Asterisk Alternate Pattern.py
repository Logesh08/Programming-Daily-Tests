# Hash - Asterisk Alternate Pattern

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary condition(s):
# 2 <= N <= 100

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 4

# Output:
# #*#*
# *#*#
# #*#*
# *#*#

# Example Input/Output 2:
# Input:
# 5

# Output:
# #*#*#
# *#*#*
# #*#*#
# *#*#*
# #*#*#



# Max Execution Time Limit: 500 millisecs





pattern = '#*'*51
n = int(input())
[print(pattern[i%2: n+i%2]) for i in range(n)]