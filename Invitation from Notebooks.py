# Invitation from Notebooks

# A boy wants to invite his N friends to his birthday party. So he decides to make N invitations. For each invitation, he needs two blue sheets and five orange sheets. A nearby store sells an infinite number of notebooks of any color, but each notebook consists of only one color with K sheets (i.e., Each notebook contains K sheets of the same color). The values of N and K are passed as the input to the program. The program must print the number of notebooks that the boy needs to buy to invite his N friends as the output.

# Boundary Condition(s):
# 1 <= N, K <= 1000

# Input Format:
# The first line contains N and K separated by a space.

# Output Format:
# The first line contains the number of notebooks based on the given conditions.

# Example Input/Output 1:
# Input:
# 3 5

# Output:
# 5

# Explanation:
# To invite 3 friends, he needs 6 blue sheets (3 x 2) and 10 orange sheets (3 x 5).
# So he buys 2 notebooks containing only blue sheets (2x5 = 10 blue sheets) and 3 notebooks containing only orange sheets (3x5 = 15 orange sheets).
# Totally, he buys 5 notebooks to invite his friends.
# Hence the output is 5

# Example Input/Output 2:
# Input:
# 15 6

# Output:
# 18



# Max Execution Time Limit: 500 millisecs



n,k = map(int,input().split())
blue = n * 2
orange = n * 5
ans = (blue // k) + (orange // k) + (1 if blue%k!=0 else 0) + (1 if orange%k!=0 else 0)
print(ans)