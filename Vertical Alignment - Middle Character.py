# Vertical Alignment - Middle Character
# The program must accept N string values as the input. The length of each string is always odd. The program must print the N string values vertically so that the middle character of each string occurs on the same line. The empty spaces must be printed as asterisks.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Length of each string <= 99

# Input Format:
# The first line contains N.
# The next N lines, each contains a string value.

# Output Format:
# The lines contain the N string values vertically based on the given conditions.

# Example Input/Output 1:
# Input:
# 4
# snake
# relaxed
# cat
# boats

# Output:
# *r**
# se*b
# nlco
# aaaa
# kxtt
# ee*s
# *d**

# Explanation:
# Here N = 4, so the given four string values are printed vertically(from top to bottom) based on the given conditions.

# Example Input/Output 2:
# Input:
# 5
# tuesday
# tea
# morning
# tests
# skillrack

# Output:
# ****s
# t*m*k
# u*oti
# etrel
# sensl
# daitr
# a*nsa
# y*g*c
# ****k










n=int(input())
arr = [input().strip() for _ in range(n)]
maxLen = len(sorted(arr,key=len)[-1])
print(maxLen)
mat=[['*' for _ in range(n)] for _ in range(maxLen)]
x,y=0,0
for i in arr:
    loop = (maxLen-len(i))//2
    for j in range(loop):
        # mat[x][y]='*'
        x+=1
    for c in i:
        mat[x][y]=c
        x+=1
    for j in range(loop):
        # mat[x][y]='*'
        x+=1
    y+=1
    x=0
for i in mat:
    print(''.join(i))