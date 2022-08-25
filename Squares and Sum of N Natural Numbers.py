# Squares and Sum of N Natural Numbers

# The program must accept an integer N as the input. The program must print the squares of natural numbers from 1. The squares must be printed up to the cube of N in the first line. The second line must contain the sum of these squares.

# Boundary Condition(s):
# 1 <= N <= 50

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the squares of N natural numbers
# The second line contains the sum of the squares of N natural numbers.

# Example Input/Output 1:
# Input:
# 5

# Output:
# 1 4 9 16 25 36 49 64 81 100 121
# 506

# Explanation:
# The N value is 5.
# The squares must be printed up to the cube of 5 that is 125.
# so the values 1 4 9 16 25 36 49 64 81 100 121 are printed.
# The sum of these squares is 506.

# Example Input/Output 2:
# Input:
# 10

# Output:
# 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961
# 10416







n = int(input())
r = n**3 
i = 1  
sum = 0
while i**2<=r:  
    print(i**2,end=' ') 
    sum += i**2
    i+=1   
print()
print(sum)  