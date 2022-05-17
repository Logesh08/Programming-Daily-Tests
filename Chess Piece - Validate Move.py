# Chess Piece - Validate Move
# An 8*8 chessboard is given below.
# a8 b8 c8 d8 e8 f8 g8 h8
# a7 b7 c7 d7 e7 f7 g7 h7
# a6 b6 c6 d6 e6 f6 g6 h6
# a5 b5 c5 d5 e5 f5 g5 h5
# a4 b4 c4 d4 e4 f4 g4 h4
# a3 b3 c3 d3 e3 f3 g3 h3
# a2 b2 c2 d2 e2 f2 g2 h2
# a1 b1 c1 d1 e1 f1 g1 h1

# The program must accept the name of a chess piece (B - Bishop or K - Knight or R - Rook) and two positions P1, P2 as the input. The program must print Yes if the given piece can move from P1 to P2. Else the program must print No as the output.

# Bishop: In Chess, a bishop can move diagonally. The movement can happen till the end of the board is reached or another piece (like Rook, Knight, Bishop, Pawn etc is encountered).

# Knight: In Chess, a knight can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L).

# Rook: In Chess, a rook can move along a row or a column. The movement can happen till the end of the board is reached or another piece (like Rook, Knight, Bishop, Pawn etc is encountered).

# Note: Assume that there are no pieces other than the given piece in the chessboard.

# Input Format:
# The first line contains the name of a chess piece.
# The second line contains the two positions P1 and P2 in the chess board.

# Output Format:
# The first line contains Yes or No.

# Example Input/Output 1:
# Input:
# B
# d4 b6

# Output:
# Yes

# Explanation:
# The given piece is Bishop.
# P1 = d4 and P2 = b6.
# The bishop can move from d4 to b6.
# Hence Yes is printed as the output.

# Example Input/Output 2:
# Input:
# K
# d4 b6

# Output:
# No

# Example Input/Output 3:
# Input:
# R
# g7 a7

# Output:
# Yes













peice = input().strip()
def convert(x):
    return (ord(x)-97)
A,B = input().split()
a,b = convert(A[0]),int(A[1])
x,y = convert(B[0]),int(B[1])
yes = 0
if peice == 'B':
    if abs(x-a)==abs(y-b) or abs(x-a) == abs(b-y):
        yes = 1
elif peice == 'R':
    if a==x or b==y:
        yes = 1
else:
    if (a==x+1 and b==y+2) or (a==x-1 and b==y-2) or (b==y+1 and a==x+2) or (b==y-1 and a==x-2):
        yes = 1
print('Yes' if yes else 'No')