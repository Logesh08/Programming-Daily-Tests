# Print String - All Eight Directions
# The program must accept a string S as the input. The program must print the string in all 8 possible directions as shown in the Example Input/Output section.

# Boundary Condition(s):
# 2 <= Length of S <= 50

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the string S in all 8 possible directions as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# CART

# Output:
# T * * T * * T
# * R * R * R *
# * * A A A * *
# T R A C A R T
# * * A A A * *
# * R * R * R *
# T * * T * * T

# Explanation:
# Here the given string is CART.
# So the string CART is printed in all 8 possible directions as given below.
# T * * T * * T
# * R * R * R *
# * * A A A * *
# T R A C A R T
# * * A A A * *
# * R * R * R *
# T * * T * * T
# The asterisks in the above pattern represent the empty spaces.

# Example Input/Output 2:
# Input:
# tiger

# Output:
# r * * * r * * * r
# * e * * e * * e *
# * * g * g * g * *
# * * * i i i * * *
# r e g i t i g e r
# * * * i i i * * *
# * * g * g * g * *
# * e * * e * * e *
# r * * * r * * * r








s=input().strip()
length=len(s)
for i in range(len(s)-1,0,-1):
    c=s[i]
    for j in range(length- i - 1):
        print('*',end = ' ')
    print(c,end=' ')
    for j in range(i-1):
        print('*',end = ' ')
    print(c,end=' ')
    for j in range(i-1):
        print('*',end = ' ')
    print(c,end=' ')
    for j in range(length- i - 1):
        print('*',end = ' ')
    print()
print(*list(s[::-1]),*list(s)[1:])
for i in range(1,length):
    c=s[i]
    for j in range(length- i - 1):
        print('*',end = ' ')
    print(c,end= ' ')
    for j in range(i-1):
        print('*',end = ' ')
    print(c,end= ' ')
    for j in range(i-1):
        print('*',end = ' ')
    print(c,end= ' ')
    for j in range(length- i - 1):
        print('*',end = ' ')
    print()