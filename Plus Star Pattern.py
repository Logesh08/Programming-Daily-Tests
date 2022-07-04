# Plus Star Pattern
# An integer N (always odd) is passed as the input to the program. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 49

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the desired pattern.

# Example Input/Output 1:
# Input:
# 5

# Output:
# *-1-*
# -*2*-
# 12345
# -*4*-
# *-5-*

# Example Input/Output 2:
# Input:
# 9

# Output:
# *---1---*
# -*--2--*-
# --*-3-*--
# ---*4*---
# 123456789
# ---*6*---
# --*-7-*--
# -*--8--*-
# *---9---*










n = int(input())
mat = [["-"]*n for _ in range(n)]
h = n//2
for i in range(n):
    mat[i][i]='*'
    mat[i][-i-1]='*'
    mat[i][h]=i+1
    mat[h][i]=i+1
for row in mat:
    print(*row,sep='')