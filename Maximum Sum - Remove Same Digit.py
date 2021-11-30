# Maximum Sum - Remove Same Digit
# The program must accept N integers as the input. The program must print the maximum sum of the integers that can be obtained by removing the same digit in all N integers.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each integer value <= 10^8

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.

# Output Format:
# The first line contains an integer value representing the maximum sum of the integers.

# Example Input/Output 1:
# Input:
# 3
# 257 9841 214

# Output:
# 10082

# Explanation:
# All possible ways are given below.
# If 1 is removed: 257 + 984 + 24 = 1265
# If 2 is removed: 57 + 9841 + 14 = 9912
# If 4 is removed: 257 + 981 + 21 = 1259
# If 5 is removed: 27 + 9841 + 214 = 10082
# If 7 is removed: 25 + 9841 + 214 = 10080
# If 8 is removed: 257 + 941 + 214 = 1412
# If 9 is removed: 257 + 841 + 214 = 1312
# The maximum sum is 10082 which is printed as the output.

# Example Input/Output 2:
# Input:
# 6
# 712 477 59 183 302 504

# Output:
# 2183





input()
arr=input().split()
s=[]
for i in range(1,10):
    cs=0
    for x in arr:
        x=list(x)
        while str(i) in x:
            x.remove(str(i))
        cs+=int(''.join(x))
    s.append(cs)
print