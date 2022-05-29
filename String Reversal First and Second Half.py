# String Reversal First and Second Half
# Given a string S, the program must reverse the first half of the string and then reverse the second of the string and print it.

# Input Format:
# The first line contains the value of string S.

# Output Format:
# The first line contains the specified output.

# Boundary Condition:
# 2 <= length of the S <= 100

# Example Input/Output 1:
# Input:
# orange

# Output:
# aroegn

# Example Input/Output 2:
# Input:
# input

# Output:
# niptu










s = input().strip()
l=len(s)
if l%2:
    print(s[:l//2][::-1]+s[l//2]+s[l//2 +1:][::-1])
else:
    print(s[:l//2][::-1]+s[l//2:][::-1])