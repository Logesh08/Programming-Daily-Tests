# Alphabet Difference Two Strings
# Given two strings S1 and S2, the program must print Yes if the alphabets in the same position in two strings differ at the most by 1 else print No.

# Boundary Condition(s):
# 1 <= Length of S1 and S2 <= 1000

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains Yes or No.

# Example Input/Output 1:
# Input:
# hello
# gemkp

# Output:
# Yes

# Example Input/Output 2:
# Input:
# best
# agts

# Output:
# No






s1=input().strip()
s2=input().strip()
for i in range(len(s1)):
    if abs(ord(s1[i])-ord(s2[i]))>1:
        print("No")
        break 
else:
    print("Yes")