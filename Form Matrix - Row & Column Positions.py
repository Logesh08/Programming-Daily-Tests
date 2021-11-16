# Form Matrix - Row & Column Positions
# The program must accept a string S containing multiple words as the input. Each word in the string S represents an element of a matrix (row position, a character and col position). The program must form a character matrix using the given string S. Then the program must print the character matrix as the output.

# Boundary Condition(s):
# 3 <= Length of S <= 10^4

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the character matrix based on the given conditions.

# Example Input/Output 1:
# Input:
# 1C3 2q2 1A1 1D4 2p1 2r3 2s4 1B2

# Output:
# A B C D
# p q r s

# Explanation:
# 1C3 -> 1st row and 3rd column -> C
# 2q2 -> 2nd row and 2nd column -> q
# 1A1 -> 1st row and 1st column -> A
# 1D4 -> 1st row and 4th column -> D
# 2p1 -> 2nd row and 1st column -> p
# 2r3 -> 2nd row and 3rd column -> r
# 2s4 -> 2nd row and 4th column -> s
# 1B2 -> 1st row and 2nd column -> B

# Example Input/Output 2:
# Input:
# 3y2 2e2 3z3 2d1 1a1 1b2 2f3 3x1 1c3

# Output:
# a b c
# d e f
# x y z





l=list(input().split())
r=[]
c=[]
x=[]
for i in l:
    t=""
    for j in i:
        if j in "1234567890":
            t+=j
            i=i[1:]
        else:
            r.append(int(t))
            c.append(int(i[1:]))
            x.append(i[0])
o=[["" for b in range(max(c))] for a in range(max(r))]
for i in zip(r,c,x):
    o[i[0]-1][i[1]-1]=i[2]
for i in o:
    print(*i)