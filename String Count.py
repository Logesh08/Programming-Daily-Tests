# String Count

# The program must accept a string S and a character matrix of size RxC as input. The program must print the count of occurrence(s) of S in the given matrix (row-wise). 

# Boundary Condition(s):
# 1 <= R, C <= 50
# 1 <= Length of the string S <= 99

# Input Format:
# The first line contains the string value S.
# The second line contains the value of R and C separated by space(s).
# The next R lines contain C characters each separated by space(s).

# Output Format:
# The first line contains the count of occurrences of S in the given matrix.

# Example Input/Output 1:
# Input:
# mango
# 6 6        
# e m a n g o
# f g h j j u
# s r q o n m
# m a n g o b
# o m m a d f
# m j i s f r

# Output:
# 2

# Example Input/Output 2:
# Input:
# oil
# 3 4
# a d o j
# c v i n
# e r l y

# Output:
# 0





# s = input().strip()
# r,c=map(int,input().split())
# mat = [''.join(input().split()) for _ in range(r)]
# count = 0
# for row in mat:
#     count += row.count(s)
# print(count)


# OneLiner
(lambda s,r: print(sum([''.join(input().split()).count(s) for _ in range(r)])))(input().strip(),int(input().split()[0]))