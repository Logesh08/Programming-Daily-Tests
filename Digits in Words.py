# Digits in Words

# The program must accept an integer N as the input. The program must print the corresponding words separated by space(s) for each digit in N as the output. The words must be printed as given below,
# 0 - zero
# 1 - one
# 2 - two
# 3 - three
# 4 - four
# 5 - five
# 6 - six
# 7 - seven
# 8 - eight
# 9 - nine

# Boundary Condition(s):
# 1 <= N <= 10^9

# Input Format:
# The first line contains the value of N.

# Output Format:
# The first line contains the words separated by space(s).

# Example Input/Output 1:
# Input:
# 100

# Output:
# one zero zero

# Example Input/Output 2:
# Input:
# 3892

# Output:
# three eight nine two






values = ['zero','one','two','three','four','five','six','seven','eight','nine']
for c in input().strip():
    print(values[int(c)],end=' ')
