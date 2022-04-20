# Matrix - Replace Asterisks in Columns
# The program must accept a matrix of size R*C as the input. The given matrix contains integers and asterisks. The number of integers in the matrix is always a multiple of R. The asterisks represent the empty spaces in the matrix. The program must rearrange the integers in the matrix so that all integers occur on the left side and all the asterisks occur on the right side of the matrix. The integers from the columns on the right(top to bottom starting from the last column) must be swapped with the asterisks on the left(top to bottom starting from the first column) of the matrix. Finally, the program must print the revised matrix as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Each integer value in matrix <= 10^5

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C values separated by a space.

# Output Format:
# The first R lines contains the revised matrix.

# Example Input/Output 1:
# Input:
# 4 4
# 11 * * 16
# * 39 75 12
# * 69 18 *
# * 79 * *

# Output:
# 11 18 * *
# 16 39 * *
# 12 69 * *
# 75 79 * *

# Explanation:
# Here R = 4 and C = 4.
# The number of integers in the matrix is 8, which is a multiple of 4.
# After rearranging the matrix based on the given conditions, the matrix becomes
# 11 18 * *
# 16 39 * *
# 12 69 * *
# 75 79 * *

# Example Input/Output 2:
# Input:
# 7 5
# * 99 89 12 *
# * 53 55 37 *
# * 23 * 91 32
# * 50 * 20 10
# * 66 * 76 85
# * 54 34 24 *
# * 45 78 58 *

# Output:
# 32 99 89 * *
# 10 53 55 * *
# 85 23 76 * *
# 12 50 24 * *
# 37 66 58 * *
# 91 54 34 * *
# 20 45 78 * *

# Example Input/Output 3:
# Input:
# 5 4
# * 23 30 61
# 87 76 * *
# * * 38 *
# * 95 25 *
# 19 * 68 *

# Output:
# 61 23 * *
# 87 76 * *
# 30 25 * *
# 38 95 * *
# 19 68 * *













r , c =map(int,input().split())
mat = [input().split() for _ in range(r)]
asrik = cur = 0

for row in mat: asrik+= row.count('*')
for i in range(c)[::-1]:
    if cur==asrik:
        break
    for j in range(r):
        if mat[j][i].isdigit():
            for x in range(c):
                for y in range(r):
                    if mat[y][x]=='*':
                        mat[y][x] = mat[j][i]
                        mat[j][i] = '*'
                        break
        cur+=1
    
for row in mat:
    print(*row)