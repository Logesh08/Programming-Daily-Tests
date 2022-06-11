# First X Vowels
# A string is passed as input. The program must print the first X vowels present in the string.
 
# Boundary Condition(s):
# 1 <= X <= 99
# 2 <= Length of String <= 1000
 
# Input Format:
# The first line contains the value of X.
# The second line contains the string.
 
# Output Format:
# The first line contains the first X vowels in the string.
 
# Example Input/Output 1:
# Input:
# 2 
# environment

# Output:
# ei

# Example Input/Output 2:
# Input:
# 3
# elephant

# Output:
# eea







n = int(input())
s = input().strip()
ctr = 0
for i in s:
    if i.lower() in "aeiou":
        print(i,end='')
        ctr+=1 
    if ctr==n: break