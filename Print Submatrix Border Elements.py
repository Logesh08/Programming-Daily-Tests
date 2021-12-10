# Print Submatrix Border Elements
# The program must accept an integer matrix R*C and two integers X and Y as the input. The integers X and Y represent the position of the top-left element of a submatrix of size (R-X+1)*(C-Y+1). The program must print the border elements of the submatrix in the clockwise direction as the output.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 1000
# 1 <= X < R
# 1 <= Y < C

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each contains C integer values separated by a space.
# The R+2nd line contains X and Y separated by a space.

# Output Format:
# The first line contains the integer values separated by a space representing the border elements of the specified submatrix in the clockwise direction.

# Example Input/Output 1:
# Input:
# 5 4
# 27 28 48 40
# 36 42 34 41
# 20 40 41 10
# 34 17 19 48
# 44 20 49 44
# 3 2

# Output:
# 40 41 10 48 44 49 20 17

# Explanation:
# Here R=5, C=4, X=3 and Y=2.
# The submatrix of size 3*3 (i.e., (5-3+1)*(4-2+1)) with the top-loft position as (3, 2) is highlighted below.
# 27 28 48 40
# 36 42 34 41
# 20 40 41 10
# 34 17 19 48
# 44 20 49 44
# So the border elements of the 3*3 submatrix are printed as the output as given below.
# 40 41 10 48 44 49 20 17

# Example Input/Output 2:
# Input:
# 6 6
# 11 26 25 32 16 50
# 12 38 36 13 27 31
# 48 33 19 34 26 27
# 17 49 38 25 23 14
# 27 10 48 50 28 47
# 20 32 39 10 18 35
# 1 3

# Output:
# 25 32 16 50 31 27 14 47 35 18 10 39 48 38 19 36












a,b=map(int,input().split())
l=[list(map(int,input().split())) for i in range(a)]
x,y=[int(i)-1 for i in input().split()]
for i in range(y,b):
    print(l[x][i],end=' ')
for i in range(x+1,a):
    print(l[i][-1],end=' ')
for i in range(b-2,y-1,-1):
    print(l[-1][i],end=' ')
for i in range(a-2,x,-1):
    print(l[i][y],end=' ')