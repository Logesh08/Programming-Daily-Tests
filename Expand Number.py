# Expand Number
# The program must accept an integer N and print the expanded number.

# Boundary Condition(s):
# 1 <= N <= 10^9

# Input Format:
# The first line contains N.

# Output Format:
# The first line contains the expanded number.

# Example Input/Output 1:
# Input:
# 5180

# Output:
# 5000+100+80

# Explanation:
# 0 is not considered.

# Example Input/Output 2:
# Input:
# 500619

# Output:
# 500000+600+10+9



n=int(input())
arr=[]
digits=0
while n>0:
    if n%10!=0:
        arr.append(n % 10 * (10**digits))
    digits+=1
    n//=10
print(*arr[::-1],sep='+')
