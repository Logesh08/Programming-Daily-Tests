# Smaller Number Based on Unit Digit
# Accept two numbers as number1 and number2. If both the unit digits are equal print the larger number. Otherwise, print the number with the smaller unit digit.

# Boundary Condition(s):
# 1 <= number1, number2 <= 99999999

# Input Format:
# The first line contains the values of number1 and number2 separated by space.

# Output Format:
# The first line contains the output number.

# Example Input/Output 1:
# Input:
# 505 725

# Output:
# 725

# Example Input/Output 2:
# Input:
# 56 8811

# Output:
# 8811









print(sorted(input().split(),key = lambda x:(int(x[-1]),-int(x)) )[0])
