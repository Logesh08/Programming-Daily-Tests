# String - Addition & Subtraction
# The program must accept a string S containing multiple words separated by the arithmetic operators + or -. The program must evaluate the given string and print the result based on the following conditions.
# - If the operator is +, then the alphabets in the right operand must be added to the left operand.
# - If the operator is -, then the alphabets in the right operand must be removed from the left operand.
# Finally, the program must print the alphabets in the resulting string in sorted order as the output.

# Note: All the alphabets in the string S are always lower case.

# Boundary Condition(s):
# 3 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains the resulting string based on the given conditions.

# Example Input/Output 1:
# Input:
# aabc-ad+db-age

# Output:
# bbc-eg

# Explanation:
# aabc - ad => abc-d
# (a is removed from the left operand, but d did not occur in the left operand so it is denoted as -d).

# (abc-d) + db => abbc
# (b is added to the left operand, d and -d cancel each other).

# abbc - age => bbc-eg
# (a is removed from the left operand, but e and g did not occur in the left operand so they are denoted as -eg).

# Example Input/Output 2:
# Input:
# skill-rack+code+learn-work

# Output:
# deeilllns-krw

# Explanation:
# skill-rack => ills-acr
# (ills-acr) + code => deillos-ar
# (deillos-ar) + learn => deeilllnos
# deeilllnos - work => deeilllns-krw

# Example Input/Output 3:
# Input:
# aabbcc-aaabcccc+aaabbbccc

# Output:
# aabbbbc