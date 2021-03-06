# Engulfed Matrix
# The program must accept an integer matrix of size R*C. The program must also accept two row values M and N and two column values P and Q. Then finally the program must print the matrix engulfed inside the rows M and N and the columns P and Q.

# Boundary Condition(s):
# 3 <= R, C <= 50
# 1 <= M, N <= R
# 1 <= P, Q <= C

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.
# The (R+2)th line contains M and N separated by a space.
# The (R+3)th line contains P and Q separated by a space.

# Output Format:
# The lines contain the matrix engulfed inside the rows M and N and the columns P and Q.

# Example Input/Output 1:
# Input:
# 5 6
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
# 41 42 43 44 45 46
# 91 92 93 94 95 96
# 4 1
# 3 6

# Output:
# 24 25
# 34 35

# Explanation:
# Here M = 4, N = 1, P = 3 and Q = 6.
# The matrix engulfed inside the rows M and N and the columns P and Q is highlighted below.
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
# 41 42 43 44 45 46
# 91 92 93 94 95 96

# Example Input/Output 2:
# Input:
# 7 7
# 75 31 61 98 70 46 62
# 42 87 19 17 91 72 88
# 35 78 19 95 63 81 30
# 93 92 53 68 84 33 22
# 73 44 62 89 79 85 55
# 16 58 46 59 45 13 69
# 55 58 44 74 29 15 48
# 2 6
# 1 5

# Output:
# 78 19 95
# 92 53 68
# 44 62 89



r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
m,n=sorted(map(int,input().split()))
p,q=sorted(map(int,input().split()))
for row in range(m,n-1):
    for col in range(p,q-1):
        print(mat[row][col],end=' ')
    print()

