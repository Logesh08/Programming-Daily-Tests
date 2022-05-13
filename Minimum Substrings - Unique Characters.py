# Minimum Substrings - Unique Characters
# The program must accept a string S containing only lower case alphabets as the input. The program must split the string into a minimal number of substrings in such a way that no alphabet occurs more than once in a substring. Then the program must print the number of substrings obtained as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains an integer representing the minimum number of substrings that can be obtained using the given conditions.

# Example Input/Output 1:
# Input:
# malayalam

# Output:
# 4

# Explanation:
# One of the possible ways is given below.
# mal - ay - al - am
# Each substring contains unique alphabets.

# Example Input/Output 2:
# Input:
# abcdbcdbaea

# Output:
# 4

# Example Input/Output 3:
# Input:
# mooon

# Output:
# 3

# Example Input/Output 4:
# Input:
# fast

# Output:
# 1












s = input().strip()
t = ''
ans = []
for c in s:
    if c in t:
        ans.append(t)
        t = c 
    else:
        t += c 
ans.append(t)
print(len(ans))