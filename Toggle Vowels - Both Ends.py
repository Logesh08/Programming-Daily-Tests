# Toggle Vowels - Both Ends
# The program must accept a string S containing only lower case alphabets as the input. The program must print the output based on the following conditions.
# - The program must toggle the first and last occurring lower case vowels to upper case in S and print the revised string as the output.
# - The program must repeat the above process till all the lower case vowels are converted to upper case in the string.

# Note: There will be at least one vowel in the string S.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the string values based on the given conditions.

# Example Input/Output 1:
# Input:
# greenapple

# Output:
# grEenapplE
# grEEnApplE

# Explanation:
# Here S = greenapple.
# So the lower case vowels in the string S are converted to upper case as given below.
# greenapple -> grEenapplE -> grEEnApplE

# Example Input/Output 2:
# Input:
# disestablishment

# Output:
# dIsestablishmEnt
# dIsEstablIshmEnt
# dIsEstAblIshmEnt

# Example Input/Output 3:
# Input:
# areyouready

# Output:
# AreyoureAdy
# ArEyourEAdy
# ArEyOUrEAdy





s = list(input().strip())
def looper(x):
    for i in x:
        if i in 'aeiou':
            return True
    return False
def getInd(x):
    for i in x:
        if i in 'aeiou':
            return x.index(i)
while looper(s):
    start = getInd(s)
    s[start] = s[start].upper()
    if looper(s):
        s=s[::-1]
        end = getInd(s)
        s[end] = s[end].upper()
        s=s[::-1]
    print(''.join(s))
    