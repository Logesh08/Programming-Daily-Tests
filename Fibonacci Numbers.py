# Fibonacci Numbers

# The program must accept N integers as input. The program must print the given integer(s) which are in the Fibonacci series.

# Boundary Condition(s):
# 1 <= N <= 100

# Input Format:
# The first line contains the integer value of N.
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the given integer(s) which are in the Fibonacci series.

# Example Input/Output 1:
# Input:
# 7
# 1 4 3 9 10 13 7

# Output:
# 1 3 13 

# Example Input/Output 2:
# Input:
# 9
# 0 2 8 5 2 1 4 13 23

# Output:
# 0 2 8 5 2 1 13 






input()
arr = list(map(int,input().split()))
n = max(arr)
n1,n2 = 0,1
fib = []
while n1<=n:
    # print(n1)
    fib.append(n1)
    nth=n1+n2
    n1=n2
    n2=nth
print(*[i for i in arr if i in fib])