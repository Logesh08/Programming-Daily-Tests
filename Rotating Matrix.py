# Rotating Matrix
# Four players A, B, C and D are playing a matrix game. They create a matrix of size N*N and then they fill the matrix with the integers from 1 to N*N (starting from 1st to Nth row where left to right in each row). The player A is sitting on the top of the matrix. The player B is sitting on the right of the matrix. The player C is sitting on the bottom of the matrix. The player D is sitting on the left of the matrix. One of the four players rotates the matrix 90-degree for X times in clockwise direction. The player who got the maximum edge sum is the winner of the game. The values of N and X as the input. The program must print the name of the winner and the sum of integers on his side of the matrix as the output.

# Boundary Condition(s):
# 2 <= N <= 50
# 1 <= X <= 10^5

# Input Format:
# The first line contains N and X separated by a space.

# Output Format:
# The first line contains the name of the winner and the sum of integers on his side of the matrix.

# Example Input/Output 1:
# Input:
# 3 2

# Output:
# A 24

# Explanation:
# Here N = 2 and X = 2.
# The four players create a 3*3 matrix as given below.
# 1 2 3
# 4 5 6
# 7 8 9

# After 1st rotation(90-degree):
# 7 4 1
# 8 5 2
# 9 6 3

# After 2nd rotation(90-degree):
# 9 8 7
# 6 5 4
# 3 2 1

# Now the player A has the maximum edge sum 24 (9 + 8 + 7).
# So player A is the winner of the game.

# Example Input/Output 2:
# Input:
# 5 15

# Output:
# B 115


# Method 1:
n,x=map(int,input().split())
x%=4
o=sum(range(n*(n-1)+1,n*n+1))
t=["C","D","A","B"]
print(t[x],o)


# Method 2:
n,x=map(int,input().split())
l=[]
for row in range(n):
    a=[]
    for col in range(1,n+1):
        a.append(row*n+col) 
    l.append(a) 
s=sum(l[-1])
if x%4==0:
    print('C',s) 
elif x%4==1:
    print('D',s) 
elif x%4==2:
    print('A',s) 
else:
    print('B',s)