# Print Sum - Integers from Ranges
# The program must accept N ranges as the input. For each range X-Y, the program must form an integer by concatenating the digits from X to Y. Then the program must print the sum of those N integers as the output.

# Boundary Condition(s):
# 2 <= N <= 100
# 0 <= X, Y <= 9

# Input Format:
# The first line contains N.
# The second line contains N ranges separated by a space.

# Output Format:
# The first line contains an integer representing the sum of the N resulting integers.

# Example Input/Output 1:
# Input:
# 3
# 5-9 2-0 7-9

# Output:
# 57788

# Explanation:
# 5-9 => 56789
# 2-0 => 210
# 7-9 => 789
# 56789 + 210 + 789 = 57788.

# Example Input/Output 2:
# Input:
# 4
# 0-9 9-0 5-1 1-5

# Output:
# 10000066665

# Explanation:
# 0-9 => 0123456789
# 9-0 => 9876543210
# 5-1 => 54321
# 1-5 => 12345
# 123456789 + 9876543210 + 54321 + 12345 = 10000066665.












input()
arr=input().split()
summ=0
for r in arr:
    t=''
    a,b=map(int,r.split('-'))
    if b>a:
        c=1
        b+=1
    else:
        c=-1
        b-=1
    for i in range(a,b,c):
        t+=str(i)
    summ+=int(t)
        
print(summ)
