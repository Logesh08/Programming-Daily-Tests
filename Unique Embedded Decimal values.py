# Unique Embedded Decimal values

# The program must accept an integer N as the input. The program must print the numbers that can be formed from the binary representation of N while traversing sequentially from start to end.
 
# Boundary Condition(s):
# 1 <= N <= 999999999

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the numbers that can be formed from the binary representation of N.

# Example Input/Output 1:
# Input:
# 12

# Output:
# 1 3 6 12 2 4 0 

# Explanation:
# The binary representation of 12 - 1100 can form the following order of binary representations 1 11 110 1100 10 100 0 in sequence.
# So, their corresponding decimal values 1 3 6 12 2 4 0 are printed as output.

# Example Input/Output 2:
# Input:
# 7 

# Output:
# 1 3 7 





n = bin(int(input()))[2:]
arr = []
for i in range(len(n)):
    for j in range(i,len(n)):
        t = int(n[i:j+1],2)
        if t not in arr:
            arr.append(t)
print(*arr)