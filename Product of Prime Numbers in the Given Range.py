# Product of Prime Numbers in the Given Range
# Accept a start value X and an end value Y as input. The program must print the product of prime numbers in the given range X and Y.

# Boundary Condition(s):
# 1 <= X, Y <= 999

# Input Format:
# The first line contains the start value and the end value.

# Output Format:
# The first line contains the product of prime numbers in the given range.

# Example Input/Output 1:
# Input:
# 2 10

# Output:
# 210

# Explanation:
# Prime numbers in the given range 2 to 10 are 2,3,5,7. Product of the prime numbers is 210 (2*3*5*7 = 210). Thus, the output is 210.

# Example Input/Output 2:
# Input:
# 30 40

# Output:
# 1147






a,b=map(int,input().split())
p=1
def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(a,b+1):
    if isPrime(i):
        p = p * i 
print(p)