# Pattern - Lower Left Plus Symbol
# Given an integer N as input, the program must print the pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains value of integer N.

# Output Format:
# The first N lines contain the pattern as shown in following examples.

# Example Input/Output 1:
# Input:
# 3

# Output:
# 3 3 3 
# + 2 2 
# + + 1 

# Example Input/Output 2:
# Input:
# 8

# Output:
# 8 8 8 8 8 8 8 8 
# + 7 7 7 7 7 7 7 
# + + 6 6 6 6 6 6 
# + + + 5 5 5 5 5 
# + + + + 4 4 4 4 
# + + + + + 3 3 3 
# + + + + + + 2 2 
# + + + + + + + 1 











n=int(input())
for i in range(n,0,-1):
    print(("+ "*(n-i))+(str(i)+" ") *i)