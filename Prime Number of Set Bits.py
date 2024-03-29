# Prime Number of Set Bits

# The program must accept two integers M and N as input. The program must print the integer(s) from M to N (inclusive) which are having the count of set bits (number of 1's) as a prime number in their binary format as the output. If there is no integer to satisfy the above conditions, then the program must print -1 as the output. 

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= M < N

# Input Format:
# The first line contains the integer value of M and N separated by a space.

# Output Format:
# The first line contains either the integer(s) which are having the count of set bits as a prime number separated by space(s) or -1.

# Example Input/Output 1:
# Input:
# 5 10

# Output:
# 5 6 7 9 10

# Explanation:
# The integers from M to N are 5 6 7 8 9 10.
# The binary representation of 5 is 101, which contains 2 set bits (number of 1's).
# 2 is a prime number. So, 5 is printed.
# The binary representation of 6 is 110, which contains 2 set bits (number of 1's).
# 2 is a prime number. So, 6 is printed. 
# The binary representation of 7 is 111, which contains 3 set bits (number of 1's).
# 3 is a prime number. So, 7 is printed. 
# The binary representation of 8 is 1000, which contains only one set bit (number of 1's).
# 1 is not a prime number. So, 8 is not printed. 
# The binary representation of 9 is 1001, which contains 2 set bits (number of 1's).
# 2 is a prime number. So, 9 is printed. 
# The binary representation of 10 is 1010, which contains 2 set bits (number of 1's).
# 2 is a prime number. So, 10 is printed. 

# Example Input/Output 2:
# Input:
# 15 16

# Output:
# -1






m,n = map(int,input().split())
p=0
for j in range(m,n+1):
    b = bin(j)[2:].count('1')
    prime = True
    for i in range(2,b):
        if b % i == 0:
            prime=False
            break
    if prime and b!=1:
        p=1
        print(j,end=' ')
if not p:
    print(-1)