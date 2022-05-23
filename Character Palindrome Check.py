# Character Palindrome Check
# Given a string S, the program must print yes if a palindrome can be formed by using all the characters in the string. Else the program must print no.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains yes or no.

# Example Input/Output 1:
# Input:
# maamd

# Output:
# yes

# Example Input/Output 2:
# Input:
# eree

# Output:
# no









s = input().strip()
od = 0
for c in set(s):
    if s.count(c)%2: od+=1
print('yes' if od==0 or od==1 else 'no')