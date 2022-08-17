# Print At Most X Factors

# An integer array of size N and an integer X are passed as the input to the program. The program must print the integers in the array which have at most X factors in the order of their occurrence. If no integer matches the given condition then the program must print -1 as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 2 <= X <= 16
# 1 <= Value of each  integer <= 99999999999999

# Input Format:
# The first line contains N and X separated by space.
# The second line contains N integers separated by space.

# Output Format:
# The first line contains the integers satisfying the given conditions separated by space.

# Example Input/Output 1:
# Input:
# 4 4
# 12 4 6 18

# Output:
# 4 6

# Example Input/Output 2:
# Input:
# 5 5
# 20 24 33 93 100

# Output:
# 33 93



n,x = map(int,input().split())
arr = list(map(int,input().split()))
for val in arr:
    fact = 0
    for i in range(1,val+1):
        if val%i == 0:
            fact += 1 
        if fact>x: break
    if fact<=x: print(val,end=' ')