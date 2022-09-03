# Odd One Out

# The program must accept an array of size N as input and it must print the position as the output in which the value differs from the other values in the evenness in the array.

# Boundary Condition(s):
# 3 <= N <= 100

# Input Format:
# The first line contains the value of N.
# The second line contains N integers separated by space(s).

# Example Input/Output 1:
# Input:
# 5
# 1 4 3 7 11

# Output:
# 2

# Explanation:
# Here 1, 3, 7 and 11 are odd numbers. Whereas 4 is an even number. So, it is the odd one among the array elements and the position of 4 is 2. Hence, 2 is printed as the output.

# Example Input/Output 2:
# Input:
# 3
# 4 6 9

# Output:
# 3




n = int(input())
arr = input().split()
odd = [i for i in arr if int(i)%2]
even = [i for i in arr if int(i)%2==0]
if len(odd)>len(even):
    print(arr.index(even[0]))
else:
    print(arr.index(odd[0]))