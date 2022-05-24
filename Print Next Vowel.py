# Print Next Vowel
# Given a string S, the program must print the next vowel present for each of the letters in the string. If there is no vowel present after the current letter then print the letter as it is.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the specified output.

# Example Input/Output 1:
# Input:
# welcome

# Output:
# eoooeee

# Example Input/Output 2:
# Input:
# different

# Output:
# ieeeeeent




s = input().strip()
for i in range(len(s)):
    c = s[i]
    i+=1
    if i==len(s): i-=1
    while True:
        if s[i] in 'aeiou':
            print(s[i],end='')
            break
        else:
            i+=1 
            if i==len(s):
                print(c,end='')
                break