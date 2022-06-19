# Replace Vowels by Preceding Consonants
# A string S is given as input. The program must replace all the vowels by its immediately preceding consonants. (Note: Print the same alphabet if no vowel is preceding it).

# Boundary Condition(s):
# 2 <= Length of String S <= 100

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains the string with only consonants.

# Example Input/Output 1:
# Input:
# telegram

# Output:
# ttllgrrm

# Example Input/Output 2:
# Input:
# yck

# Output:
# yck










s = input().strip()
l = len(s)
for i in range(l):
    t = s[i]
    while i>=0 and s[i].lower() in "aeiou":
        i-=1
    if i<0: s[i]=t
    print(s[i],end='')