# Decremented Value of M

# The program must accept two integers M and N as input. The program must decrement the value of M for N times. If the unit digit of M is 0, then divide M by 10. The program must print the final decremented value as the output.

# Boundary Condition(s):
# 1 <= M <= 999999999
# 1 <= N <= 99

# Input Format:
# The first line contains the integer values of M and N separated by space(s).

# Output Format:
# The first line contains the final decremented value of M.

# Example Input/Output 1:
# Input
# 412 4

# Output
# 40

# Explanation:
# After the first decrement, M = 411.
# After the second decrement, M = 410.
# During the third decrement, unit digit of M is 0 so divide M by 10.
# After the third decrement, M = 41.
# After the fourth decrement, M = 40.
# Thus, 40 is printed as the output.

# Example Input/Output 2:
# Input:
# 12000 3

# Output:
# 12







m,n=map(int,input().split())
for i in range(n):
    if m%10==0:
        m//=10 
    else:
        m-=1 
print(m)
