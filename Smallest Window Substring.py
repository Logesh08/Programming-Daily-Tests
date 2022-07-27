# Smallest Window Substring

# The program must accept two string values S1 and S2 as input. The program must print the smallest substring in the string S1 which contains all the alphabets in the string S2. If there is no such substring in the string S1 then the program must print -1. 

# Note: If more than one smallest substring has the same length then consider the first substring.

# Boundary Condition(s):
# 1 <= Length of S1 <= 1000
# 1 <= Length of S2 <= Length of S1

# Input Format:
# The first line contains the two string values S1 and S2 separated by a space.

# Output Format:
# The first line contains the smallest substring of S1 or -1.

# Example Input/Output 1:
# Input:
# abodecodebanc abc

# Output:
# banc

# Explanation:
# The substrings of abodecodebanc which contains abc are abodec, bodecodeba, codeba and banc.
# Hence the output is smallest substring banc

# Example Input/Output 2:
# Input:
# environment nee

# Output:
# environme

# Example Input/Output 3:
# Input:
# helloworld cd

# Output:
# -1







def isValid(S1,S2):
    for ch in S2:
        if ch not in S1:
            return False
        S1=S1.replace(ch,"",1)
    return True
S1,S2=input().split()
for L in range(len(S2),len(S1)+1):
    for index in range(len(S1)-L+1):
        if isValid(S1[index:index+L],S2):
            print(S1[index:index+L])
            exit()
print(-1)