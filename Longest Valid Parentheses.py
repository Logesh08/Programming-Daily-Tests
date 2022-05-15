# Longest Valid Parentheses
# The program must accept a string S containing only parentheses. The program must print the length of the longest substring having the valid parentheses(balanced parentheses) in the given string as the output. If there is no such substring, then the program must print 0 as the output.

# Boundary Condition(s):
# 1 <= Length of S <= 1000

# Input Format:
# The first line contains S.

# Output Format:
# The first line contains an integer representing the length of the longest substring having the balanced parentheses.

# Example Input/Output 1:
# Input:
# )(()))(())())

# Output:
# 6

# Explanation:
# The longest substring having the balanced parentheses is highlighted below.
# )(()))(())())

# Example Input/Output 2:
# Input:
# ))(((

# Output:
# 0










s = input().strip()
if len(s) == 0 : exit()
        
stack = [-1]
res = 0

for i, c in enumerate(s):
    if c == '(':
        stack.append(i)
    else:
        stack.pop()
        if len(stack) == 0:
            stack.append(i)
        else:
            res = max(res, i - stack[-1])
print(res)