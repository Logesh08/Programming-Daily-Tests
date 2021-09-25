# Prime Numbers - Three Digits
# The program must accept 3 distinct digits a, b and c. The program must print all possible prime numbers (1, 2 or 3 digits) that can be formed with these three digits.
# The prime numbers must be sorted.

# Note: There will be at least one prime number formed using the given three digits.

# Boundary Condition(s):
# 0 <= a, b, c <= 9

# Input Format:
# The first line contains a, b and c separated by a space.

# Output Format:
# The first line contains all possible prime numbers separated by a space that can be formed with the given three digits.

# Example Input/Output 1:
# Input:
# 3 0 1

# Output:
# 3 13 31 103

# Explanation:
# Here a=3, b=0 and c=1.
# All the possible numbers that can be formed with the digits 3, 0 and 1 are given below.
# 0 -> not a prime number
# 1 -> not a prime number
# 3 -> prime number
# 10 -> not a prime number
# 13 -> prime number
# 30 -> not a prime number
# 31 -> prime number
# 103 -> prime number
# 130 -> not a prime number
# 301 -> not a prime number
# 310 -> not a prime number
# Hence the output is
# 3 13 31 103

# Example Input/Output 2:
# Input:
# 7 3 5

# Output:
# 3 5 7 37 53 73


from itertools import permutations
from math import sqrt
x=[]
l=input().strip().split()
for i in range(1,4):
    p=permutations(l,i)
    for j in p:
        print(j)
        val=int(''.join(j))
        flag=1
        if(val>1):
            for r in range(2,int(sqrt(val))+1):
                if(val%r==0):
                    flag=0
                    break
            if(flag):
                x.append(val)
print(*sorted(set(x)))
