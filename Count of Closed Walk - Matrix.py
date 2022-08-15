# Count of Closed Walk - Matrix

# The program must accept an integer matrix of size MxM and an integer N representing the size of NxN submatrix as input. The program must print the count of NxN submatrices in the MxM matrix whose border elements are even integers.

# Boundary Condition(s):
# 3 <= M <= 50
# 2 <= N <= M

# Input Format:
# The first line contains the values of M and N.
# The next M lines contain M integers each separated by space(s).

# Output Format:
# The first line contains the count of the NxN submatrices in the MxM matrix whose border elements are even integers.

# Example Input/Output 1:
# Input:
# 5 3
# 2 1 2 2 2
# 2 2 4 4 2
# 6 4 6 6 2
# 2 2 2 1 1
# 2 3 1 1 1

# Output:
# 2

# Explanation:
# Two sub matrices with all border even elements of size 3x3 are
# 2 2 2
# 4 4 2
# 6 6 2
# and
# 2 2 4
# 6 4 6
# 2 2 2

# Example Input/Output 2:
# Input:
# 4 2
# 1 2 30 41
# 10 12 14 16
# 8 62 40 66
# 2 22 31 6

# Output:
# 5









m,n = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(m)]
count = 0
for i in range(m - n + 1):
    for j in range(m - n +1 ):
        flag = True
        for x in range(i,i+n):
            if mat[x][j]%2 or mat[x][j+n -1]%2:
                flag = False
                break
        for y in range(j,j+n):
            if mat[i][y]%2 or mat[i +n -1][y]%2:
                flag = False
                break
        if flag:
            count += 1
print(count)