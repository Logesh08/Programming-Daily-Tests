# Top-Left to Bottom-Right Diagonals Pattern
# The program must accept an integer N as the input. The program must form a grid of hyphens of size (N^2)*(N^2). Then the program must replace the top-left to bottom-right diagonal in each N*N subgrid with asterisks. Finally, the program must print the (N^2)*(N^2) grid as the output.

# Boundary Condition(s):
# 1 <= N <= 15

# Input Format:
# The first line contains N.

# Output Format:
# The first N*N lines contain the pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 2

# Output:
# * - * -
# - * - *
# * - * -
# - * - *

# Explanation:
# Here N=2, so the pattern contains 4 lines(2*2) of output and each line contains 4 characters(2*2) separated by a space.
# In the 4*4 grid of hyphens, the top-left to bottom-right diagonal of each 2*2 subgrid is replaced with asterisks.

# Example Input/Output 2:
# Input:
# 3

# Output:
# * - - * - - * - -
# - * - - * - - * -
# - - * - - * - - *
# * - - * - - * - -
# - * - - * - - * -
# - - * - - * - - *
# * - - * - - * - -
# - * - - * - - * -
# - - * - - * - - *



n=int(input())
s=""
count=0
for i in range(n*n):
    if count==0:
        s+="*"
        count=n-1
    else:
        s+="-"
        count-=1
for i in range(n*n):
    for c in s[-i:]:
        print(c,end=" ")
    if i!=0:
        for c in s[:-i]:
            print(c,end=" ")
    print()
