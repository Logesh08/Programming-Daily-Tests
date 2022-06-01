# Median of Three Integers
# Three integers A, B and C are passed as input. The program must print the median element of the input. If no median element can be calculated the program must print -1.

# Boundary Condition(s):
# 1 <= A, B, C <= 99999999

# Input Format:
# The first line contains A, B and C separated by space(s).

# Output Format:
# The first line contains the median element.

# Example Input/Output 1:
# Input:
# 34 12 45

# Output:
# 34

# Example Input/Output 2:
# Input:
# 21 34  21

# Output:
# -1






a,b,c = map(int,input().split())
if len(set([a,b,c]))<3:
    print(-1)
else:
    print(sorted([a,b,c])[1])