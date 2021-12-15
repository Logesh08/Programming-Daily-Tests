# Find Sum - Expanded Integers
# The program must accept N string values containing only nonzero digits as the input, where each string S represents an integer value but each digit D in the integer is repeated D times. The program must find the original integer values from the given string values. Then the program must print the sum of the resulting N integers as the output.
# Note: The value of each integer(i.e., the value after converting the string to an integer) can be from 1 to 999999.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains N.
# The next N lines, each contains a string value representing an integer value but each digit D in the integer is repeated D times.

# Output Format:
# The first line contains an integer value representing the sum of the resulting N integers.

# Example Input/Output 1:
# Input:
# 4
# 13334444
# 2222
# 44449999999994444
# 555556666661333

# Output:
# 6263

# Explanation:
# 13334444 -> 134.
# 2222 -> 22.
# 44449999999994444 -> 494.
# 555556666661333 -> 5613.
# 134 + 22 + 494 + 5613 = 6263.

# Example Input/Output 2:
# Input:
# 3
# 88888888
# 122122
# 44447777777

# Output:
# 1267

# Explanation:
# 88888888 -> 8.
# 122122 -> 1212.
# 44447777777 -> 47.
# 8 + 1212 + 47 = 1267.






n=int(input())
summ=0
for i in range(n):
    t=''
    s =  input().strip()
    length , i = len(s) , 0
    while i<length:
        c=s[i]
        t += (s[i])
        i+=int(c)
    summ+=int(t)
print(summ)