# Last Box Picked by the Poet

# A king was happy with the skills of a poet and hence wanted to reward him. The king placed N boxes in a straight line each with certain number of gold coins in it. The poet can pick the boxes starting from the last. If the number on the box has the unitdigit as zero, then it is the last box that the poet can pick. Else, the poet can pick the boxes placed in the straight line by skipping the boxes by unitdigit of the number on the box. The program must print the last box picked by the poet as the output. Note: The poet cannot skip and move further than the first box in that case he must pick the first box.

# Boundary Condition(s):
# 2 <= N <= 99

# Input Format:
# The first line contains the value of N.
# The second line contains the N integers separated by space.

# Output Format:
# The first line contains the last box picked by the poet.

# Example Input/Output 1:
# Input:
# 5
# 11 21 31 51 61

# Output:
# 11

# Example Input/Output 2:
# Input:
# 7
# 29 32 43 54 61 70 81

# Output:
# 70






input()
arr = input().split()
for i in arr[::-1]:
    if i[-1]=='0':
        print(i)
        exit()
print(arr[0])