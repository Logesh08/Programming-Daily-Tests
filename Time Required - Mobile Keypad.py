# Time Required - Mobile Keypad
# There are 9 keys in a mobile. The 9 keys are arranged as a 3*3 matrix as shown below.
# 1 2 3
# 4 5 6
# 7 8 9

# The program must accept a string S containing only nonzero digits indicating the digits to be typed on the mobile. To type the first digit in S, it takes 0 seconds. To type the next digit, it takes 1 second if the next digit is an adjacent digit(in all 8 possible directions). If the next digit is equal to the current digit, it takes 0 seconds. Otherwise, it takes 2 seconds. The program must print the number of seconds it takes to type the string S as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 100

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains an integer value representing the number of seconds it takes to type the string S.

# Example Input/Output 1:
# Input:
# 146591

# Output:
# 7

# Explanation:
# 1 -> 0 seconds (1st digit)
# 4 -> 1 second (1 and 4 are adjacent)
# 6 -> 2 seconds (4 and 6 are not adjacent)
# 5 -> 1 second (5 and 6 are adjacent)
# 9 -> 1 second (5 and 9 are adjacent)
# 1 -> 2 seconds (9 and 1 are not adjacent)

# Example Input/Output 2:
# Input:
# 812398721

# Output:
# 11





