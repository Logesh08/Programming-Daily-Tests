# All Submatrices Sum - From Top-Left
# The program must accept an integer matrix of size R*C as the input. The program must find all possible submatrices starting from the top-left cell of the given matrix. Then the program must print the sum of each submatrix as shown in the Example Input/Output section.

# Hint: Optimize your logic to avoid Time Limit Exceeded Error.

# Boundary Condition(s):
# 2 <= R, C <= 500
# 1 <= Matrix element value <= 10^4

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space representing the R*C matrix.

# Output Format:
# The first R lines, each contains C integers separated by a space representing the of submatrices sum based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 1 3 6
# 5 12 21
# 12 27 45

# Explanation:
# 1 -> (1)
# 3 -> (1+2)
# 6 -> (1+2+3)
# 5 -> (1+4)
# 12 -> (1+2+4+5)
# 21 -> (1+2+3+4+5+6)
# 12 -> (1+4+7)
# 27 -> (1+2+4+5+7+8)
# 45 -> (1+2+3+4+5+6+7+8+9)

# Example Input/Output 2:
# Input:
# 4 5
# 70 40 20 50 20
# 30 10 60 50 90
# 80 60 20 60 70
# 10 30 30 10 10

# Output:
# 70 110 130 180 200
# 100 150 230 330 440
# 180 290 390 550 730
# 190 330 460 630 820











r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
for i in range(r):
    p=0
    for j in range(c):
        if i!=0:
            mat[i][j]+=mat[i-1][j]
            
        p += mat[i][j]
        print(p,end=' ')
    print()