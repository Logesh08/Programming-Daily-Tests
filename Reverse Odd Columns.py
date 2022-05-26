# Reverse Odd Columns
# Given a matrix of size NxN, the program must reverse the columns present in odd positions of the matrix and print the matrix.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.
# The next N lines contain the matrix.

# Output Format:
# The first N line contains the specified output.

# Example Input/Output 1:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 7 2 9
# 4 5 6
# 1 8 3

# Example Input/Output 2:
# Input:
# 4
# 12 56 89 555
# 76 332 22 17
# 77 33 77 99
# 56 56 29 48

# Output:
# 56 56 29 555
# 77 332 77 17
# 76 33 22 99
# 12 56 89 4



n = int(input())
mat = [input().split() for _ in range(n)]
mat = list(map(list,zip(*mat)))
for i in range(n):
    if i % 2==0: mat[i] = mat[i][::-1]
mat = list(map(list,zip(*mat)))
for row in mat: print(*row)