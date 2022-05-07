# Matrix - Spirally Palindrome
# The program must accept a character matrix of size R*C as the input. The program must form a string S by traversing the matrix spirally in the clockwise direction. The program must print YES if S is a palindrome. Else the program must print NO as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C characters separated by a space.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# 6 5
# A b c d e
# m l k J f
# n c b i g
# o d A h h
# o e f g i
# n m l k J

# Output:
# YES

# Explanation:
# The string obtained by traversing the 6*5 matrix in the spiral clockwise direction is AbcdefghiJklmnoonmlkJihgfedcbA.
# Here, the string AbcdefghiJklmnoonmlkJihgfedcbA is a palindrome.
# So YES is printed.

# Example Input/Output 2:
# Input:
# 7 8
# m c i a r a t o
# l l e w e u a n
# p X y r u V r g
# E r u j n w y k
# m s v m x n t g
# q i g p l w d j
# u t s n c g a K

# Output:
# NO

# Example Input/Output 3:
# Input:
# 3 3
# m a k
# a m e
# k e r

# Output:
# YES






R,C= map( int, (input()) .split())
mat = [input().split() for _ in range(R)]
visited = [[0]*C for _ in range(R)] 
RR,CC = R,C
i = j = 0
r = 0
c = 1
START = 0
t=''
while True:
    if not visited[i][j]: 
        visited[i][j] = 1 
        t+=(mat[i][j]) 
        i += r  
        j += c  
        
    else:
        Sum = 0
        i+=1 
        j+=1
        try:
            if not visited[i][j]:
                R -= 1 
                C -= 1 
                START += 1
            else:
                break
        except:
            break
    if j==C:
        c=0
        r=1
        j -= 1
        i += 1
    elif i==R:
        c = -1
        r = 0
        i -= 1
        j -= 1
    elif j<START:
        c = 0
        r = -1
        j += 1
        i -= 1
    elif i<START:
        r = 0
        c = 1
        i += 1
        j+=1
if not visited[RR//2][CC//2]:
    t+=mat[RR//2] [CC//2]
print('YES' if t==t[::-1] else 'NO')
 







 ## Other solution:
R,C=map(int,input().split())
matrix=[input().split() for row in range(R)]
stRow,stCol,endRow,endCol=0,0,R-1,C-1
S=""
while stRow<endRow and stCol<endCol:
    for col in range(stCol,endCol+1):
        S+=matrix[stRow][col]
    for row in range(stRow+1,endRow+1):
        S+=matrix[row][endCol]
    for col in range(endCol-1,stCol-1,-1):
        S+=matrix[endRow][col]
    for row in range(endRow-1,stRow,-1):
        S+=matrix[row][stCol]
    stRow+=1 
    endRow-=1 
    stCol+=1 
    endCol-=1
if stCol==endCol and stRow!=endRow:
    for row in range(stRow,endRow+1):
        S+=matrix[row][stCol]
elif stRow==endRow and stCol!=endCol:
    for col in range(stCol,endCol+1):
        S+=matrix[stRow][col]
elif R==C and R%2!=0:
    S+=matrix[R//2][C//2]
print("YES" if S==S[::-1] else "NO")