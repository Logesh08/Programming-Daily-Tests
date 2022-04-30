# Matrix - Column wise Pattern
# The program must accept an integer matrix of size R*C as the input. The program must print the digits of each integer in the matrix column wise as shown in the Example Input/Output section.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 10^5

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integers separated by a space.

# Output Format:
# The lines contain the digits of each integer in the matrix column wise as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 3 3
# 66 70 42
# 13 64 55
# 76 10 15

# Output:
# 6 7 4
# 6 0 2
# 1 6 5
# 3 4 5
# 7 1 1
# 6 0 5

# Explanation:
# Here R = 3 and C = 3.
# The digits of each integer in the matrix are printed column wise as given below.
# 6 7 4
# 6 0 2
# 1 6 5
# 3 4 5
# 7 1 1
# 6 0 5

# Example Input/Output 2:
# Input:
# 2 3
# 7 4 1
# 5 685 98

# Output:
# 7 4 1
# 5 6 9
# * 8 8
# * 5 *

# Example Input/Output 3:
# Input:
# 3 3
# 5 457 15
# 1 987 4
# 9 33 2

# Output:
# 5 4 1
# 1 5 5
# 9 7 4
# * 9 2
# * 8 *
# * 7 *
# * 3 *
# * 3 *









## Method 1
r,c=map(int,input().split())
mat=[list(input().split()) for i in range(r)]
mat=["".join(list(x)) for x in zip(*mat)]
while any(mat):
    for i in range(c):
        if mat[i]:
            print(mat[i][0],end=" ")
            mat[i]=mat[i][1:]
        else:
            print("*",end=" ")
    print()

## Method 2
R , C = map(int,input().split())
matrix = [input().split() for _ in range(R)]
colDigs = []
for col in zip(*matrix):
    currCol = []
    for num in col:
        for dig in num:
            currCol.append(dig)
    colDigs.append(currCol)
maxLen = len(max(colDigs,key = len))
for index in range(C):
    while(len(colDigs[index]) < maxLen):
        colDigs[index].append("*")
for row in zip(*colDigs):
    print(*row)

## Failed
r,c = map(int,input().split())
mat = [input().split() for _ in range(r)]
ans = []
for row in mat:
    m = max(list(map(len,row)))
    s = [['*']*c for _ in range(m)]
    # print(s)
    for i in range(len(row)):
        val=row[i]
        for j in range(len(val)):
            s[j][i] = val[j]
    for row in s:
        ans.append(row)
        
for i in range(len(ans)):
    for j in range(c):
        while i>0 and ans[i][j]!='*' and ans[i-1][j]=='*':
            ans[i-1][j],ans[i][j] = ans[i][j],ans[i-1][j]
            i-=1
            
for row in ans:
    print(*row)