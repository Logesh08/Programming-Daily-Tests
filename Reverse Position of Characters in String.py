# Reverse Position of Characters in String
# A string S is passed as the input to the program. The program must transform each alphabet in the string to the alphabet present at the reverse position. The space must be retained in same position without any modification.

# Boundary Condition(s):
# 1 <= Length of String S <= 1000

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains the string with the reverse position of characters.

# Example Input/ Output 1:
# Input:
# abc yz

# Output:
# zyx ba

# Example Input/Output 2:
# Input:
# dza

# Output:
# waz






s = input().strip()
alpha = ""
for i in range(ord('a'),ord('z')+1):
    alpha+=chr(i)
rev = alpha[::-1]
for c in s:
    if c.isalpha():
        print(alpha[rev.index(c)],end='')
    else:
        print(c,end='')
