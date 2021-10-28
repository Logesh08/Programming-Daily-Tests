# Find Matrix Size
# The program must accept the integer values representing vertically concatenated integer matrices(possibly one) as the input. For each matrix, the program must print the size as the output.

# Input Format:
# The lines, each contains the integer values separated by a space representing vertically concatenated integer matrices.

# Output Format:
# The lines, each contains two integer values representing the size of a matrix.

# Example Input/Output 1:
# Input:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 10 20
# 30 40
# 50 60
# 70 80 90
# 12 45 78

# Output:
# 3 4
# 3 2
# 2 3

# Explanation:
# The size of the first integer matrix is 3*4.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# The size of the first integer matrix is 3*2.
# 10 20
# 30 40
# 50 60

# The size of the first integer matrix is 2*3.
# 70 80 90
# 12 45 78

# Example Input/Output 2:
# Input:
# 80 88 54 15 97
# 6 80 68 6 14
# 15 85 72 47 65
# 18 99 46 62 26
# 3 62 67 75 45
# 1 79 63 62 52

# Output:
# 6 5

# Example Input/Output 3:
# Input:
# 10
# 20
# 30
# 40
# 50 60 70 80
# 90
# 100
# 11 12
# 13 14
# 15

# Output:
# 4 1
# 1 4
# 2 1
# 2 2
# 1 1






a=list(map(int,input().split()))
r=1;c=len(a)
while(True):
    try:
        a=list(map(int,input().split()))
        if len(a)!=c:
            print(r,c)
            r=1
            c=len(a)
        else:
            r+=1 
    except:
        print(r,c)
        break