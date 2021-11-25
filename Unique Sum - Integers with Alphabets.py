# Unique Sum - Integers with Alphabets
# The program must accept N string values as the input. Each string represents an integer value but only one lower case alphabet is mixed into the integer. The program must find the unique integers among the given N string values. The duplicate integers contain identical alphabets (For example, 12a5 and 1a25 are duplicates, but 12a5 and 12b5 are distinct). Then the program must print the sum of those unique integers as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 2 <= Length of each string <= 8

# Input Format:
# The first line contains N.
# The second line contains N string values separated by a space.

# Output Format:
# The first line contains an integer value representing the sum of the resulting unique integers.

# Example Input/Output 1:
# Input:
# 6
# 1a23 5b6 5c6 a78 123a b123

# Output:
# 436

# Explanation:
# There are 5 unique integers based on the lower case alphabets.
# 123 -> (1a23 or 123a)
# 56 -> 5b6
# 56 -> 5c6
# 78 -> a78
# 123 -> b123
# The sum of the resulting unique integers = 436 (123 + 56 + 56 + 78 + 123)

# Example Input/Output 2:
# Input:
# 5
# 6h547 65h47 6a547 654b7 6547h

# Output:
# 19641




n=int(input())
a=input().split()
m=[]
for i in range(n):
    d=""
    al=""
    for j in a[i]:
        if j.isdigit():
            d+=j
        else:
            al+=j
    k=[int(d),al]
    if k not in m:
        m.append(k)
print(sum([i[0] for i in m]))