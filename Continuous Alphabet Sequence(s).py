# Continuous Alphabet Sequence(s)
# Given a string S as the input, the program must print the continuous alphabet sequences in the string S. Else the program must print -1 if there is no continuous alphabet sequence in the string.

# Boundary Condition(s):
# 2 <= Length of S <= 100

# Input Format:
# The first line contains the string S.

# Output Format:
# The first line contains the continuous alphabet sequence(s) in the string or -1.

# Example Input/Output 1:
# Input:
# habcuedyzab

# Output:
# abcyzab

# Explanation:
# The continuous alphabet sequences in the string are abc yzab
# Hence the output is abcyzab

# Example Input/Output 2:
# Input:
# wmhhfygogd

# Output:
# -1

# Explanation:
# There is no continuous alphabet sequence in the string.
# Hence the output is -1







s = input().strip()
t = s[0]
arr = []
for i in range(1,len(s)):
    if ord(s[i]) == ord(s[i - 1])+1 or (t[-1]=='z' and s[i]=='a'):
        t += s[i]
    else:
        if len(t)>1:
            arr.append(t)
        t = s[i]
if len(t)>1:
    arr.append(t)
print(''.join(arr) if arr else -1)