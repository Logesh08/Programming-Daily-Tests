# String to Grids
# The program must accept two integers N, X and a string S as the input. The length of the string S is always N*N. The value of X is always odd. The program must form a grid of asterisks of size (N*X)*(N*X). For each X*X subgrid, the program must replace the middle element with the corresponding character in the string S(left to right). Finally, the program must print the revised grid as the output.

# Boundary Condition(s):
# 1 <= N, X <= 25

# Input Format:
# The first line contains N and X separated by a space.
# The second line contains S.

# Output Format:
# The first N*X lines contain the grid based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 3
# SkillRack

# Output:
# * * * * * * * * *
# * S * * k * * i *
# * * * * * * * * *
# * * * * * * * * *
# * l * * l * * R *
# * * * * * * * * *
# * * * * * * * * *
# * a * * c * * k *
# * * * * * * * * *

# Explanation:
# Here N = 3 and X = 3.
# So 9*9 grid of asterisks is formed as given below.
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
# After replacing the middle elements in the 3*3 subgrids with the characters of S, the grid becomes
# * * * * * * * * *
# * S * * k * * i *
# * * * * * * * * *
# * * * * * * * * *
# * l * * l * * R *
# * * * * * * * * *
# * * * * * * * * *
# * a * * c * * k *
# * * * * * * * * *

# Example Input/Output 2:
# Input:
# 2 5
# DONE

# Output:
# * * * * * * * * * *
# * * * * * * * * * *
# * * D * * * * O * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * N * * * * E * *
# * * * * * * * * * *
# * * * * * * * * * *

# Example Input/Output 3:
# Input:
# 4 3
# abcdefghijklmnop

# Output:
# * * * * * * * * * * * *
# * a * * b * * c * * d *
# * * * * * * * * * * * *
# * * * * * * * * * * * *
# * e * * f * * g * * h *
# * * * * * * * * * * * *
# * * * * * * * * * * * *
# * i * * j * * k * * l *
# * * * * * * * * * * * *
# * * * * * * * * * * * *
# * m * * n * * o * * p *
# * * * * * * * * * * * *





n,x=map(int,input().split()) 
s=input().strip() 
length=n*x
l=[['*']*(length) for i in range(length)] 
ind=0
for i in range(0,length-x+1,x):
    for j in range(0,length-x+1,x):
        l[i+x//2][j+x//2]=s[ind]
        ind+=1 
[print(*i) for i in l]