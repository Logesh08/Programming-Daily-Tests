# Next D Alphabets Circularly - String
# The program must accept a string S containing only alphabets and nonzero digits. For each digit D in the string S, the program must print the next D alphabets in the string S. Consider the alphabets in circular fashion when printing the next D alphabets in the string S.

# Boundary Condition(s):
# 2 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The lines, each contains a string value.

# Example Input/Output 1:
# Input:
# 9skill4rack6

# Output:
# skillrack
# rack
# skillr

# Explanation:
# Here the given string is 9skill4rack6.
# The 1st digit is 9, so the next 9 alphabets s, k, i, l, l, r, a, c and k are printed.
# The 2nd digit is 4, so the next 4 alphabets r, a, c and k are printed.
# The 3rd digit is 6, so the next 6 alphabets s, k, i, l, l and r are printed.

# Example Input/Output 2:
# Input:
# Wat99er1

# Output:
# erWaterWa
# erWaterWa
# W








s=input().strip()
for i in range(len(s)):
    c=s[i]
    if c.isdigit():
        counter = 0
        ind = i
        while counter < int(c):
            if ind >= len(s): ind = 0
            if s[ind].isalpha():
                print(s[ind],end='')
                counter+= 1
            ind+= 1
        print()