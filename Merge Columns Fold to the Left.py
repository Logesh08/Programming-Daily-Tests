# Merge Columns Fold to the Left
# An integer matrix with R rows and C columns is passed as the input. The programs must fold the matrix towards the left starting from the Nth column and merge(add the cell values) the overlapping column values. Then the program must print the resulting matrix.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^4
# 1 <= N <= C

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space.
# The R+2nd line contains N.

# Output Format:
# The first R lines contain the folded matrix based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 5
# 10 20 30 40 50
# 99 77 55 44 11
# 1 3 5 6 9
# 4

# Output:
# 10 70 70
# 99 88 99
# 1 12 11

# Explanation:
# The matrix must be folded from the fourth column towards the left. So the 4th column will merge with the 3rd column.
# The 5th column will merge with the 2nd column. 
# So the 3rd column values are 30+40=70, 55+44=99 and 5+6=11.
# The 2nd column values are 20+50=70, 77+11=88 and 3+9=12.

# Example Input/Output 2:
# Input:
# 3 5
# 1 2 3 4 5
# 4 8 6 7 9
# 10 20 30 45 55
# 2

# Output:
# 5 4 3 3
# 9 7 6 12
# 55 45 30 30

# Example Input/Output 3:
# Input:
# 3 5
# 1 2 3 4 5
# 2 4 6 8 2
# 10 20 30 40 50
# 1

# Output:
# 5 4 3 2 1
# 2 8 6 4 2
# 50 40 30 20 10






# Method 1
n,m=map(int,input().split())
b=[list(map(int,input().split())) for i in range(n)]
v=int(input())
c=[]
for i in range(n):
    cc=[]
    for j in range(v-1,m):
        cc+=[b[i][j]]
    c+=[cc]
for i in range(n):
    jj=0
    for j in range(v-2,-1,-1):
        if jj<m-v+1:
            c[i][jj]+=b[i][j]
        else:
            c[i]+=[b[i][j]]
        jj+=1
for i in c:
    print(*i[::-1])









# Method 2
r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
nthcol=int(input())
currcol=nthcol-2 
ans=[[] for i in range(r)] 
for col in range(nthcol-1,c):
    for row in range(0,r):
        if currcol>=0:
            ans[row].insert(0,mat[row][currcol]+mat[row][col]) 
        else:
            ans[row].insert(0,mat[row][col])
    currcol-=1 
for col in range(currcol,-1,-1):
    for row in range(0,r):
        ans[row].insert(0,mat[row][col])

for i in ans:
    print(*i)