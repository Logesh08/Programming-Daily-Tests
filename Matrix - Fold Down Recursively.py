# Matrix - Fold Down Recursively
# The program must accept an integer matrix of size R*C as the input. The value of R is always even. The program must print the output based on the following conditions.
# - The program must fold the matrix downwards and merge(add the cell values) the overlapping row values. Then the program must print the resulting matrix.
# - Then the program must repeat the above process on the resulting matrix till the number of rows of the matrix becomes odd.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^5

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.

# Output Format:
# The lines contain the resulting matrices.

# Example Input/Output 1:
# Input:
# 8 5
# 3 6 5 4 3
# 4 8 7 7 1
# 5 5 3 2 2
# 3 2 5 3 2
# 5 9 1 9 4
# 7 2 2 2 7
# 7 4 8 6 3
# 6 6 4 2 1

# Output:
# 8 11 6 12 6
# 12 7 5 4 9
# 11 12 15 13 4
# 9 12 9 6 4
# 23 19 20 17 13
# 17 23 15 18 10
# 40 42 35 35 23

# Explanation:
# Here R = 8 and C = 5.

# 1st fold down:
# 8 11 6 12 6
# 12 7 5 4 9
# 11 12 15 13 4
# 9 12 9 6 4

# 2nd fold down:
# 23 19 20 17 13
# 17 23 15 18 10

# 3rd fold down:
# 40 42 35 35 23

# Example Input/Output 2:
# Input:
# 6 2
# 10 10
# 20 20
# 30 30
# 11 11
# 22 22
# 33 33

# Output:
# 41 41
# 42 42
# 43 43







r,c=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
tmp = mat.copy()
while r  % 2 == 0:
    mat = tmp.copy()
    tmp = [[0]*c for _ in range(r//2)]
    for i in range(r//2):
        for j in range(c):
            tmp[i][j]=(mat[i+r//2][j]+mat[(r//2) - i -1][j])
            print(mat[i+r//2][j]+mat[(r//2) - i -1][j],end=' ')
        print()
    r//=2