# Integer Box Sum Pattern

# The program must accept two integers X and Y as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s):
# 1 <= X < Y <= 1000

# Input Format:
# The first line contains X and Y separated by a space.

# Output Format:
# The lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:
# Input:
# 1 5

# Output:
# +--+
# |01|
# |02|
# |03|
# |04|
# |05|
# +--+
# |15|
# +--+

# Example Input/Output 2:
# Input:
# 110 113

# Output:
# +---+
# |110|
# |111|
# |112|
# |113|
# +---+
# |446|
# +---+



# Max Execution Time Limit: 500 millisecs



a,b=map(int,input().split())
arr = [i for i in range(a,b+1)]
Max = len(str(sum(arr)))
def line():
    print('+'+'-'*Max+'+')
def Print(i):
    print(f'|{str(i).zfill(Max)}|') 
line()
[Print(i) for i in arr]
line()
Print(sum(arr))
line()