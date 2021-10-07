# Flip Coin - Head and Tail
# Hector is playing a game with a coin. The coin has two faces HEAD and TAIL. He tosses the coin N times. The number of times the coin is flipped in each toss is passed as the input. After each toss, he uses the face obtained in the previous toss to start the next toss. The program also accepts a character F representing the initial face of the coin. Finally, the program must print the number of times he gets HEAD and the number of times he gets TAIL as the output.

# Boundary Condition(s):
# 1 <= N <= 100
# 1 <= Each Integer value <= 1000

# Input Format:
# The first line contains N.
# The second line contains N integer values separated by a space.
# The third line contains a character F.

# Output Format:
# The first line contains two integer values representing the number of times he gets HEAD and the number of times he gets TAIL.

# Example Input/Output 1:
# Input:
# 5
# 3 3 4 5 2
# H

# Output:
# 2 3

# Explanation:
# Initially, the coin face = HEAD.
# After the 1st toss, the coin face = TAIL.
# After the 2nd toss, the coin face = HEAD.
# After the 3rd toss, the coin face = HEAD.
# After the 4th toss, the coin face = TAIL.
# After the 5th toss, the coin face = TAIL.
# He got the HEAD twice and the TAIL thrice.
# Hence the output is
# 2 3

# Example Input/Output 2:
# Input:
# 6
# 4 2 10 5 3 4
# T

# Output:
# 1 5


n=int(input())
arr=list(map(int,input().split()))
start=input().strip()
head=tail=0
if start=="H":
    cur=1
else:
    cur=0
for i in arr:
    if i&1:
        if cur==1:
            cur=0
            tail+=1
        else:
            cur=1
            head+=1
    else:
        if cur==1:
            head+=1
        else:
            tail+=1
print(head,tail)