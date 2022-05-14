# Brick Wall Pattern
# The program must accept four integers L, H, R and C as the input. The integers L and H represent the length and height of a brick. The integer R represents the number of rows of bricks in the wall to be constructed. The integer C represents the number of bricks in each row of the wall to be constructed. A mason wants to construct a wall of size R*C using two types of bricks based on the following conditions.
# - In the Rth row, the mason places the type I bricks and type II bricks alternately.
# - In the R-1st row, the mason places half of the type II brick on the left and then he follows the order of bricks in the Rth row.
# - In the R-2nd row, the mason places the type II bricks and type I bricks alternatively.
# - In the R-3rd row, the mason places half of the type I brick on the left and then he follows the order of bricks in the R-2nd row.
# - Similarly, the mason repeats the order of bricks in the bottom four rows to construct the remaining rows of the wall.
# The type I bricks must be represented by the asterisks(*) and the type II bricks must be represented by the hash symbols(#).
# Finally, the program must print the wall constructed by mason as the output.

# Note: The value of L is always even.

# Boundary Condition(s):
# 2 <= L, H <= 50
# 1 <= R, C <= 50

# Input Format:
# The first line contains L and H separated by a space.
# The second line contains R and C separated by a space.

# Output Format:
# The first R*H lines, each contains C*L characters.

# Example Input/Output 1:
# Input:
# 6 2
# 7 4

# Output:
# ######******######******
# ######******######******
# ###******######******###
# ###******######******###
# ******######******######
# ******######******######
# ***######******######***
# ***######******######***
# ######******######******
# ######******######******
# ###******######******###
# ###******######******###
# ******######******######
# ******######******######

# Explanation:
# Here L = 6, H = 2, R = 7 and C = 4.
# The type I brick is given below.
# ******
# ******

# The type II brick is given below.
# ######
# ######

# So the 7*4 wall is constructed based on the given conditions.

# Example Input/Output 2
# Input:
# 8 2
# 10 5

# Output:
# ####********########********########****
# ####********########********########****
# ********########********########********
# ********########********########********
# ****########********########********####
# ****########********########********####
# ########********########********########
# ########********########********########
# ####********########********########****
# ####********########********########****
# ********########********########********
# ********########********########********
# ****########********########********####
# ****########********########********####
# ########********########********########
# ########********########********########
# ####********########********########****
# ####********########********########****
# ********########********########********
# ********########********########********












l,h = map(int,input().split())
r,c = map(int,input().split())
t1='*'*(l//2 )
t2='#'*(l//2)
for i in range(r):
    for _ in range(h):
        for j in range(c):
            if i%4==0:
                if j%2:
                    print(t1*2,end='') 
                else:
                    print(t2*2,end='') 
            elif i%4==2:
                if j%2:
                    print(t2*2,end='') 
                else:
                    print(t1*2,end='') 
            elif i%4==1:
                m = 2 
                if j==0: m = 1
                if j%2:
                    print(t1*m,end='') 
                else:
                    print(t2*m,end='')
                if j==c-1:
                    print(t2,end='') 
            else:
                m = 2 
                if j==0: m = 1
                if j%2:
                    print(t2*m,end='') 
                else:
                    print(t1*m,end='')
                if j==c-1:
                    print(t1,end='') 
        print()
    