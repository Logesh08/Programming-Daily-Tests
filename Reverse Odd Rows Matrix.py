# Reverse Odd Rows Matrix
# Given a matrix M of size N*N, the program must reverse the order of odd rows and print it.

# Input Format:
# The first line contains the value of N.
# The next N lines contain N elements each separated by space.

# Output Format:
# The first N lines contain the matrix with odd rows reversed.

# Boundary Condition:
# 2 <= N <= 50

# Example Input/Output 1:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 3 2 1
# 4 5 6
# 9 8 7

# Example Input/Output 2:
# Input:
# 2
# 10 20
# 40 50

# Output:
# 20 10
# 40 50




n=int(input())
mat = [input().split() for _ in range(n)]
for i in range(n):
    if i%2==0:
        print(*mat[i][::-1])
    else:
        print(*mat[i])