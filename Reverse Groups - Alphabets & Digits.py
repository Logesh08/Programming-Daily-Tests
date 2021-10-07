# Reverse Groups - Alphabets & Digits
# The program must accept a string S containing only alphabets and digits as the input. The program must reverse every group of alphabets and every group of digits in the string S. Then the program must print the revised string S as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the revised string.

# Example Input/Output 1:
# Input:
# abcd1234skillrack994xyz

# Output:
# dcba4321kcarlliks499zyx

# Explanation:
# 1st group (alphabets): abcd -> dcba
# 2nd group (digits): 1234 -> 4321
# 3rd group (alphabets): skillrack -> kcarlliks
# 4th group (digits): 994 -> 499
# 5th group (alphabets): xyz -> zyx

# Example Input/Output 2:
# Input:
# a1b10cd4ef56

# Output:
# a1b01dc4fe65




s=input().strip()
temp=""+s[0]
vals=[]
for i in range(1,len(s)):
    if (s[i-1].isalpha() and s[i].isalpha()) or (s[i-1].isdigit() and s[i].isdigit()):
        temp+=s[i]
    else:
        vals.append(temp)
        temp=""+s[i]
vals.append(temp)
[print(i[::-1],end='') for i in vals]



