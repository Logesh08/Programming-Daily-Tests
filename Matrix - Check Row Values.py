# Matrix - Check Row Values
# The program must accept an R*C integer matrix. Let N=R*C. The program must check if the matrix contains all values from 1 to N. It must also check if Row 1 contains at least one of the values from 1 to C, Row 2 contains at least one of the values from C+1 to 2C and so on till checking if Row R contains at least one of the values from (R-1)*C+1 to N. If the matrix satisfies all these conditions it must print Yes. Else it must print No as the output.

# Boundary Condition(s):
# 1 <= R, C <= 100

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines, each containing C values separated by a space.

# Output Format:
# The first line contains Yes or No.

# Example Input/Output 1:
# Input:
# 3 4
# 5 6 3 8
# 1 2 10 7
# 11 9 12 4

# Output:
# Yes

# Explanation:
# N = 3*4 = 12. All the values from 1 to 12 are present.
# 1st row contains 3 (that is for at least one value from 1 to 4).
# 2nd row contains 7 (that is for at least one value from 5 to 8).
# 3rd row contains 9, 11, 12 (that is for at least one value from 9 to 12).
# As all the conditions are satisfied the output is Yes.

# Example Input/Output 2:
# Input:
# 3 4
# 5 6 3 8
# 1 2 10 12
# 11 9 7 4

# Output:
# No


m,n=map(int,input().split())
s=[list(map(int,input().split())) for i in range(m)]
k=[]
for i in s:
    k+=i 
t=[i for i in range(1,m*n+1)]
if sorted(k)!=t:
    print("No")
    exit()
while t:
    for x in t[:n]:
        if x in s[0]:
            f=1
            break 
    else:
        print("No")
        exit()
    t=t[n:]
    s=s[1:]
print("Yes")
