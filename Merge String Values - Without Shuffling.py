# Merge String Values - Without Shuffling
# The program must accept two string values S1 and S2 as the input. Both S1 and S2 represent a string but each character is repeated a certain number of times. The program must merge the given two string values without any shuffle in the order of occurrences of the characters.

# Boundary Condition(s):
# 1 <= Length of S1, S2 <= 100

# Input Format:
# The first line contains S1.
# The second line contains S2.

# Output Format:
# The first line contains a string value representing the merged string.

# Example Input/Output 1:
# Input:
# aabbbcca
# aaabbccccaaa

# Output:
# aaaaabbbbbccccccaaaa

# Explanation:
# S1 = "aabbbcca"
# S2 = "aaabbccccaaa"
# aa & aaa -> aaaaa
# bbb & bb -> bbbbb
# cc && cccc -> cccccc
# a & aaa -> aaaa
# Hence the output is
# aaaaabbbbbccccccaaaa

# Example Input/Output 2:
# Input:
# abcaaaabbcc
# aaabbbcccabc

# Output:
# aaaabbbbccccaaaaabbbccc






a=input().strip()
b=input().strip()
ind=0
p=a[0]
a1,b1=[],[]
t=a[0]
for i in range(1,len(a)):
    if a[i]==p:
        t+=a[i]
    else:
        a1.append(t)
        t=''
        t+=a[i]
    p=a[i]
a1.append(t)
t=b[0]
p=b[0]
for i in range(1,len(b)):
    if b[i]==p:
        t+=b[i]
    else:
        b1.append(t)
        t=''
        t+=b[i]
    p=b[i]
b1.append(t)
for i in range(len(a1)):
    print(a1[i]+b1[i],end='')
