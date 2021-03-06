# First N Terms - Powers of 7
# The program must accept an integer N as the input. The program must print the first N terms in the following series.
# 1, 7, 8, 49, 50, 56, 57, 343, .... and so on.
# Each integer in the above series is a power of 7 or sum of unique powers of 7. All integers in the series are always sorted in ascending order.

# Boundary Condition(s):
# 1 <= N <= 1000

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains the first N terms in the given series.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 1 7 8 49 50

# Explanation:
# 1st term: 7^0 = 1
# 2nd term: 7^1 = 7
# 3rd term: 7^1 + 7^0 = 8
# 4th term: 7^2 = 49
# 5th term: 7^2 + 7^0 = 50

# Example Input/Output 2:
# Input:
# 10

# Output:
# 1 7 8 49 50 56 57 343 344 350










n=int(input())
l=[];c=0
while len(l)<n:
    s=7**c;k=[s]
    for j in range(len(l)):
        k.append(s+l[j])
    l+=k;c+=1
print(*sorted(l)[:n])