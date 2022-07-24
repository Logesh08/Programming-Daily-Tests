# Print Xth Number that can be formed with digits in N

# The program must accept two integers N and X as input. The program must print the Xth number from 1 which can be formed using the digits in N. If there is no Xth number then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N, X <= 999999999

# Input Format:
# The first line contains the value of N.        
# The second line contains the value of X.

# Output Format:
# The first line contains the Xth number or -1.

# Example Input/Output 1:
# Input:
# 231
# 9

# Output:
# 32

# Explanation:
# The N = 123 forms the sequential order of numbers are 1 2 3 12 13 21 23 31 32 123 132 213 231 312 321.
# Then, the 9th number in the sequence is 32.
# So, 32 is printed as the output.

# Example Input/Output 2:
# Input:
# 100
# 4

# Output:
# -1

# Explanation:
# The N = 100 forms the sequential order of numbers are 1 10 100.
# Hence there is no 4th number.
# S0, -1 is printed as the output.







from itertools import permutations
n = list(input().strip())
x = int(input())
c = 0
for j in range(len(n)):
    perm = permutations(n,j+1)
    for i in list(perm):
        c += 1
        if c==x:
            print((''.join(i)))
            exit()
print(-1)