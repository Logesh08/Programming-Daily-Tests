 # Toggle Vowel

# A string S containing only alphabets is passed as the input to the program. The program must toggle the case of vowels at odd positions and print the string.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains the String S.

# Output Format:
# The first line contains the string with vowels toggled at the odd positions.

# Example Input/Output 1:
# Input:
# cool

# Ouput:
# coOl

# Explanation :
# vowel 'o' in 3rd position is toggled.

# Example Input/Output 2:
# Input:
# URANIUM

# Ouput:
# uRaNiUM

# Explanation :
# vowels 'U' is in 1st , 'A' is in 3rd and 'I' is in 5th positions are toggled.







s = input().strip()
for i in range(len(s)):
    if i%2==0 and s[i].lower() in "aeiou":
        print(s[i].swapcase())
    else:
        print(s[i],end='')