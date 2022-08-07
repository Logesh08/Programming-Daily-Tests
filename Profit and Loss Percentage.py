# Profit and Loss Percentage

# The program must accept N numbers of cost price, selling price and an integer M as input. The program must print the count of profit percentage and loss percentage which is greater than or equal to M.

# Boundary Condition(s):
# 2 <= N, M <= 50

# Input Format:
# The first line contains the value of N.
# The next N lines contain cost price and selling price.
# The (N + 2)th line contains the value of M.

# Output Format:
# The first line contains the number of profit percentage and loss percentage which are greater than M percentage.

# Example Input/Output 1:
# Input:
# 4
# 100 80
# 20 90
# 30 15
# 50 55
# 20

# Output:
# 1 2

# Explanation:
# The loss percentage of 100 and 80 is 20.
# The profit percentage of 20 and 90 is 350.
# The loss percentage of 30 and 15 is 50.
# The profit percentage of 50 and 55 is 10.
# The profit percentage is greater than M (20) is 350, so the count 1 is printed.
# The loss percentage is greater than or equal to M (20) are 20 and 50, so the count 2 is printed.

# Example Input/Output 2:
# Input:
# 5
# 90 100
# 1500 2000
# 120 100
# 30 10
# 2000 2100
# 50

# Output:
# 0 1










n=int(input())
prices = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
p=l=0
for i in prices:
    cp = i[0]
    i = sorted(i)
    percent = ((i[1]-i[0])/cp) * 100
    if percent>=m:
        if cp==i[0]:
            p += 1 
        else:
            l += 1 
print(p,l)