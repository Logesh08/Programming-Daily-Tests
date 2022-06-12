# Matrix - Printing Center Element
# Given an integer matrix of size N*N, print the elements present at the center of the matrix.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains the value of N.
# The next N lines contain N elements each separated by space(s).

# Output Format:
# The program must print the output as specified in Example Input/Output section.

# Example Input/Output 1:
# Input:
# 4
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2 
# 3 4 5 6

# Ouput:
# 6 7 
# 0 1

# Example Input/Output 2:
# Input:
# 3
# 1 2 3 
# 5 6 7 
# 9 0 1 

# Ouput:
# 6 
 
 
 


 
n = int(input())
mat = [input().split() for _ in range(n)]
if n%2:
    print(mat[n//2][n//2])
else:
    print(mat[n//2 -1][n//2 -1],mat[n//2-1][n//2])
    print(mat[n//2][n//2 -1],mat[n//2][n//2])