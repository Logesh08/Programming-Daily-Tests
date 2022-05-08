# Super Digit Integer
# The program must accept an integer N as the input. 
# The program must print YES if the given integer N is a super digit integer. 
# Else the program must print NO as the output.

# A super digit integer is an integer N such that D*(ND) contains a substring made of D digits D (where 2 <= D <= 9).

# Boundary Condition(s):
# 1 <= N <= 10^8

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains YES or NO.

# Example Input/Output 1:
# Input:
# 753

# Output:
# YES

# Explanation:
# If D = 3, then 3 * (753^3) = 3 * (753 * 753 * 753) = 1280873331.
# The result 1280873331 contains three 3s.
# Hence YES is printed as the output.

# Example Input/Output 2:
# Input:
# 333

# Output:
# YES

# Explanation:
# If D = 2, then 2 * (333^2) = 2 * (333 * 333) = 221778.
# The result 221778 contains two 2s.
# Hence YES is printed as the output.

# Example Input/Output 3:
# Input:
# 1170

# Output:
# NO






n = int(input())
for i in range(2,10):
    if str(i)*i in str(i*(n**i)) :
        print('YES')
        exit()
print('NO')