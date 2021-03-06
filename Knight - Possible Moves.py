# Knight - Possible Moves
# The program must accept the position of a Knight (Horse) in a chessboard denoted by the letter 'H' and print the number of moves M it can make from that position. Assume no other pieces are on the chessboard which are denoted by the letter 'B'.
# Note: In Chess, a knight can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L).

# Input Format:
# 8 lines and one line among them containing the letter H.

# Output Format:
# The first line contains M.

# Example Input/Output 1:
# Input:
# B B B B B B H B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B

# Output:
# 3

# Explanation:
# The positions where the Knight can move are indicated by '*'.
# B B B B B B H B
# B B B B * B B B
# B B B B B * B *
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# As three moves are possible, 3 is printed as the output.

# Example Input/Output 2:
# Input:
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B H B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B
# B B B B B B B B

# Output:
# 8

# Explanation:
# The 8 moves are indicated by asterisk '*'.
# B B B B B B B B
# B B * B * B B B
# B * B B B * B B
# B B B H B B B B
# B * B B B * B B
# B B * B * B B B
# B B B B B B B B



horses=[[1,-2],[2,-1],[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[-2,1]]
chess = [input().split() for _ in range(8)]
count=0
for row in range(8):
    for col in range(8):
        if chess[row][col]=='H':
            for posA,posB in horses:
                if 0<= row+posA < 8 and 0<=col+posB<8:
                    count+=1 
print(count)