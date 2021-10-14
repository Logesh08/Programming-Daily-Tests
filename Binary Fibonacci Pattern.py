# Binary Fibonacci Pattern
# The program must accept an integer N as the input. The program must print the Binary Fibonacci pattern of (2*N)-1 lines based on the following conditions.
# - The first line contains 0.
# - The second line contains 1.
# - Each line from 3 to N contains the concatenation of previous two lines.
# - The remaining N-1 lines contain the water image of the first N-1 lines.

# Boundary Condition(s):
# 3 <= N <= 20

# Input Format:
# The first line contains N.

# Output Format:
# The first (2*N)-1 lines contain the Binary Fibonacci pattern.

# Example Input/Output 1:
# Input:
# 6

# Output:
# 0
# 1
# 01
# 101
# 01101
# 10101101
# 01101
# 101
# 01
# 1
# 0

# Explanation:
# Here N=6, so the pattern contains 11 lines ((2*6)-1) of output.
# In the 1st line, 0 is printed.
# In the 2nd line, 1 is printed.
# In the 3rd line, 01 (i.e., the concatenation of 0 and 1) is printed.
# In the 4th line, 101 (i.e., the concatenation of 1 and 01) is printed.
# In the 5th line, 01101 (i.e., the concatenation of 01 and 101) is printed.
# In the 6th line, 10101101 (i.e., the concatenation of 101 and 01101) is printed.
# The next 5 lines contain the water image of the first 5 lines.

# Example Input/Output 2:
# Input:
# 9

# Output:
# 0
# 1
# 01
# 101
# 01101
# 10101101
# 0110110101101
# 101011010110110101101
# 0110110101101101011010110110101101
# 101011010110110101101
# 0110110101101
# 10101101
# 01101
# 101
# 01
# 1
# 0





n=int(input()) 
l=["0","1"] 
for i in range(3,n+1): 
    l.append(l[-2]+l[-1]) 
for i in l: 
    print(i) 
for i in l[:-1][::-1]: 
    print(i)