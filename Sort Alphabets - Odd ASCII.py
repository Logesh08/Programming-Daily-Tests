# Sort Alphabets - Odd ASCII
# The program must accept a string S containing only alphabets as the input. The program must sort the alphabets having odd ASCII values in their positions and keep the other alphabets in their same positions in the string S. Then the program must print the modified string S as the output.

# Boundary Condition(s):
# 2 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the modified string S.

# Example Input/Output 1:
# Input:
# skillrack

# Output:
# acillrkks

# Explanation:
# Here S = "skillrack".
# The alphabets that are having the odd ASCII values are s, k, i, a, c and k.
# After sorting the alphabets based on the given conditions, the string becomes acillrkks.
# Hence the output is acillrkks.

# Example Input/Output 2:
# Input:
# DOWNLOAD

# Output:
# DAONLOWD











s = list(input().strip())
arr = []
srt = []
for i in s:
    if ord(i)%2:
        srt.append(i)
        arr.append('*')
    else:
        arr.append(i)

srt = sorted(srt,key = lambda x: ord(x))
for i in arr:
    if i=='*':
        print(srt.pop(0),end='')
    else:
        print(i,end='')