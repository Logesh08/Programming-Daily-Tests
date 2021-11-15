# Arrange String Values - Middle Alphabet
# The program must accept a string S containing only unique alphabets and N string values as the input. All N string values have an equal odd length. For each alphabet in S, the program must print the string having the same alphabet(ignoring case) in its middle. If there is no such string, then the program must print asterisks except the middle alphabet.

# Note: There will be no string value with the same alphabet in the middle.

# Boundary Condition(s):
# 1 <= N <= Length of S <= 26
# 1 <= Length of each string <= 99

# Input Format:
# The first line contains S.
# The second line contains N.
# The next N lines, each contains a string value.

# Output Format:
# The lines, each contains a string value.

# Example Input/Output 1:
# Input:
# pencil
# 4
# yield
# paper
# hills
# white

# Output:
# paper
# yield
# **n**
# **c**
# white
# hills

# Explanation:
# Here S = "pencil" and N = 4.
# p -> paper
# e -> yield
# n -> **n** (no strings with n in the middle)
# c -> **c** (no strings with c in the middle)
# i -> white
# l -> hills

# Example Input/Output 2:
# Input:
# ZAbc
# 2
# DOMAINS
# CHECKUP

# Output:
# ***Z***
# DOMAINS
# ***b***
# CHECKUP






s=input().strip()
n=int(input())
l=[input().strip() for i in range(n)]
for i in range(len(s)):
    f=0
    for j in range(n):
        if l[j][len(l[j])//2].lower()==s[i].lower():
            print(l[j])
            f=1 
            break 
    if f==0:
        print('*'*(len(l[0])//2)+s[i]+'*'*(len(l[0])//2))