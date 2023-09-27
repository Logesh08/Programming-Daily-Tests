# Buy X Get Y Free

# In a supermarket, there is an offer for chocolates to attract customers. The offer is "BUY X GET Y FREE" (i.e., If a customer buys X chocolates then he/she takes Y chocolates for free). This special offer can be used any number of times. The cost of each chocolate is M rupees. A boy has N rupees and he wants to get as many chocolates for free. The values of X, Y, M and N are passed as the input. The program must print the maximum number of chocolates he can buy from N rupees as the output.

# Boundary Condition(s):
# 1<= X, Y, M, N <= 10^8

# Input Format:
# The first line contains X, Y, M and N values separated by a space.

# Output Format:
# The first line contains the maximum number of chocolates.

# Example Input/Output 1:
# Input:
# 2 1 1 4

# Output:
# 6

# Explanation:
# The cost of a chocolate is 1 rupee.
# OFFER: BUY 2 GET 1 FREE. if he buys 2 chocolates then he gets 1 chocolate for free.
# The boy can buy 4 chocolates for 4 rupees and 2 chocolates for free. So he can buy 6 chocolates.
# Hence the output is 6

# Example Input/Output 2:
# Input:
# 2 2 3 11

# Output:
# 5




x,y,m,n = map(int,input().split())
chokis = n//m
buffer = chokis
while buffer >= x:
    new = (buffer//x)*y
    chokis += new
    buffer = new
    break
print(chokis)
