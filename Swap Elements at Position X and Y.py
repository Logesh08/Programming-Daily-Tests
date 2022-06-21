# Swap Elements at Position X and Y
# Accept an integer array of size N as input. The program must swap elements at positions X and Y. Then the program must print them.

# Boundary Condition(s):
# 2 <= X, Y <= 99

# Input Format:
# The first line contains the value of N, X and Y separated by space(s).
# The second line contains N integers separated by space(s).

# Output Format:
# The first line contains the array with elements swapped at positions X and Y.

# Example Input/Output 1:
# Input: 
# 10 3 6
# 100 200 300 400 500 600 700 800 900 1000

# Output:
# 100 200 600 400 500 300 700 800 900 1000

# Example Input/Ouput 2:
# Input:
# 4 2 4
# 35 46 57 68

# Output:
# 35 68 57 46







n,x,y = map(int,input().split())
arr = input().split()
arr[x-1],arr[y-1]=arr[y-1],arr[x-1]
print(*arr)