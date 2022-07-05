# Pattern Printing - Mirror Image with Hyphens
# Accept a number N as the input. The program must print the mirror image pattern as the shown in the Example Input/Output section.

# Boundary Condition(s):
# 3 <= N <= 30

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first N lines contain the mirror image pattern.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 55555-55555
# 4444---4444
# 333-----333
# 22-------22
# 1---------1

# Example Input/output 2:
# Input:
# 4

# Output:
# 4444-4444
# 333---333
# 22-----22
# 1-------1










n = int(input())
for i in range(n)[::-1]:
    print(str(i+1)*(i+1),'-'*(((n-i-1)*2)+1),str(i+1)*(i+1),sep='')