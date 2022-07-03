# Consonants in the Odd Position
# Accept a string S as the input. If the odd position has consonants then the program must print the corresponding characters along with their ASCII value, same characters in upper case and their ASCII value as output. (Note: Input will be in lowercase only)                                                                            
# Boundary Condition(s):
# 1 <= Length of String S <= 100

# Input Format:
# The first line contains the string S.

# output Format:
# The consonants with their ASCII value and corresponding uppercase character with ASCII value are printed on each line.

# Example Input/Output 1:
# Input:
# chocolate

# Output:
# c 99 C 67

# Example Input/Output 2:
# Input:
# enlighten

# Output:
# l 108 L 76
# g 103 G 71
# t 116 T 84
# n 110 N 78







s = input().strip()
arr = [s[i] for i in range(len(s)) if i%2==0 and s[i] not in 'aeiou']
for c in arr:
    print(c,ord(c),c.upper(),ord(c.upper()))