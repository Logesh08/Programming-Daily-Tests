# String Formation Count

# The program must accept two string values of S1 and S2 as the input. The program must print the number of times S2 can be formed using the alphabets from S1.

# Boundary Condition(s):
# 2 <= Length of String S1 <= 1000
# 2 <= Length of String S2 <= 100

# Input Format:
# The first line contains the value of string S1.
# The second line contains the value of string S2.

# Output Format:
# The first line contains the number of times the string S2 can be formed with the alphabets from the string S1.

# Example Input/Output 1:
# Input:
# hheelloojhsell
# hello

# Output:
# 2

# Explanation:
# h is repeated 3 times.
# e is repeated 3 times.
# l is repeated 4 times.
# o is repeated 2 times.
# So, hello can be formed 2 times from the string hheelloojhsell.

# Example Input/Output 2:
# Input:
# he rides cycle
# he

# Output:
# 1






a = input().strip()
b = input().strip()
arr = []
for c in set(b):
    arr.append(a.count(c))
print(min(arr))




# OneLiner
(lambda x,y: print(min([x.count(c) for c in set(y)])))(input(),input())