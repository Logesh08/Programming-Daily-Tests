# Common Vowels in S1
# Two string values S1 and S2 are passed as the input to the program. The program must print each alphabet in string S1 only if the alphabet is a vowel and also it is present in string S2.

# Boundary Condition(s):
# 1 <= Length of String S1, S2 <= 1000

# Input Format:
# The first line contains the string S1.
# The second line contains the string S2.

# Output Format:
# The first line contains the vowels as per the given conditions.

# Example input/Output 1:
# Input:
# umbrella
# amenity

# output:
# ea

# Example Input/Output 2:
# Input:
# meet
# feet

# Output:
# ee




a = input().strip()
b = input().strip()
for i in a:
    if i.lower() in 'aeiou' and i in b:
        print(i,end='')