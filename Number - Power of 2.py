# Number - Power of 2
# A positive integer N is passed as the input. The program must print YES if N is a power of 2. Else the program must print NO.

# Boundary Condition(s):
# 1 <= N <= 999999999999999

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains YES or NO

# Example Input/Output 1:
# Input:
# 16

# Output:
# YES

# Example Input/Output 2:
# Input:
# 12

# Output:
# NO











def isPowerOfTwo(n): 
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
print('YES' if isPowerOfTwo(int(input())) else 'NO')