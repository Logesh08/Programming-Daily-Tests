# Equivalent Diagonal Matrix
# Given an integer matrix of size NxN, the program must print yes if all the elements of the left diagonal are present in right diagonal and also all the elements of the right diagonal are present in left diagonal otherwise print no.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.
# The next N lines contain the matrix.

# Output Format:
# The first line contains yes or no.

# Example Input/Output 1:
# Input:
# 3
# 12 34 56
# 78 90 29
# 12 68 56

# Output:
# yes

# Example Input/Output 2:
# Input:
# 4
# 27 91 78 34 
# 1 13 12 7 
# 18 54 64 73 
# 72 67 77 8 

# Output:
# no














n=int(input())
mat = [input().split() for _ in range(n)]
left,right=[],[]
for i in range(n):
    left.append(mat[i][i])
    right.append(mat[i][n-i-1])
print('yes' if sorted(set(left))==sorted(set(right)) else 'no')
