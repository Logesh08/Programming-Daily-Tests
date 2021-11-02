# Simplify Polynomial Expression
# The program must accept a string S representing a polynomial expression. The program must simplify the given polynomial expression by combining the like terms (i.e., combining the terms having the same exponent values). Then the program must print the simplified polynomial expression. The terms in the simplified polynomial must be sorted by their exponent values in descending order. If there are no terms in the simplified polynomial expression, then the program must print 0 as the output.

# Boundary Condition(s):
# 5 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the simplified polynomial expression or 0.

# Example Input/Output 1:
# Input:
# -4x^1+3x^2-7x^0+9x^1-12x^2-5x^4

# Output:
# -5x^4-9x^2+5x^1-7x^0

# Explanation:
# +3x^2 and -12x^2 are combined as -9x^2.
# -4x^1 and +9x^1 are combined as 5x^1.
# So the simplified polynomial expression is -5x^4-9x^2+5x^1-7x^0.

# Example Input/Output 2:
# Input:
# +105x^3+5x^5+99x^4-105x^3+5x^5-10x^5

# Output:
# +99x^4

# Example Input/Output 3:
# Input:
# +1x^1-2x^50-1x^1+2x^50

# Output:
# 0




s=input().strip()+" "
d=dict()
while 'x' in s:
    i=s.index("x")
    a=s[:i]
    c=1
    b=s[i+2]
    while s[i+c+2] in "1234567890":
        b+=s[i+c+2]
        c+=1
    a,b=int(a),int(b)
    if b in d:
        d[b]+=a
    else:
        d[b]=a
    s=s[i+c+2:]
l=sorted(list(d),reverse=True)
f=1
for i in l:
    if d[i]!=0:
        if d[i]>0:
            print("+",end="")
            print(d[i],end="")
            print("x^",end="")
            print(i,end="")
            f=0
        else:
            print(d[i],end="")
            print("x^",end="")
            print(i,end="")
            f=0
if f:print(0)