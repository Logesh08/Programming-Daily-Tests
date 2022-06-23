# Sum of Addition Subtraction And Multiplication
# Given two integers A and B as input, the program must find the sum of A and B then find the difference of A and B then find the product of A and B at last print the sum of all the result.

# Boundary Condition(s):
# 1 <= A, B <= 999999999

# Input Format:
# The first line contains the value of A and B separated by space(s).

# Output Format:
# The first line contains the value of sum.

# Example Input/Output 1:
# Input:
# 5 4

# Output:
# 30

# Example Input/Output 2:
# Input:
# 6 8

# Output:
# 60









a,b = map(int,input().split())
mul = a*b 
sub = (a-b)
sum = a+b
print(mul+sub+sum)