# Reducing Triangular Wave Pattern
# The program must accept an integer N as the input. The program must print the reducing triangular wave pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 3 <= N <= 50

# Input Format:
# The first line contains N.

# Output Format:
# The first N lines contain the reducing triangular wave pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 5

# Output:
# #
# * # * * * * * #
# * * # * * * # * # * #
# * * * # * # * * * #
# * * * * #

# Explanation:
# Here N=5, so the pattern contains 5 lines of reducing triangular wave pattern.

# Example Input/Output 2:
# Input:
# 8

# Output:
# #
# * # * * * * * * * * * * * #
# * * # * * * * * * * * * # * # * * * * * * * #
# * * * # * * * * * * * # * * * # * * * * * # * # * * * #
# * * * * # * * * * * # * * * * * # * * * # * * * # * # * #
# * * * * * # * * * # * * * * * * * # * # * * * * * #
# * * * * * * # * # * * * * * * * * * #
# * * * * * * * #





x=int(input())
print('#')
f=[[] for a in range(x-1)]
for t in range(x//2):
    n=1
    if t==0:
        for a in range(t,x-1-t):
            for b in range(a+1):
                f[a].append('*')
            f[a].append('#')
    else:
        for a in range(t,x-t-1):
            for b in range(n):
                f[a].append('*')
            n+=2
            f[a].append('#')
    n=1
    for a in range(x-t-3,t-1,-1):
        for b in range(n):
            f[a].append('*')
        n+=2
        f[a].append('#')
for a in f:
    print(*a)