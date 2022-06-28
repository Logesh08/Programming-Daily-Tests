# Print Date
# A series of dates is passed as input. The dates are in the format of day/month/year The program must print the historically largest date. Ignore the invalid dates. If all the dates are invalid print -1.

# Boundary Condition(s):
# 0 <= DD, MM, YYYY <= 999999

# Input Format:
# The first line contains the dates separated by space(s).

# Output Format:
# The first line contains the historically largest date in format DD/MM/YYYY.

# Example Input/Output 1:
# Input:
# 2/4/2000 4/11/2018 22/12/2018 24/12/2018 22/12/1996

# Output:
# 24/12/2018

# Example Input/Output 2:
# Input:
# 29/14/1997 32/7/1996 15/8/1990 24/1/1999

# Output:
# 24/01/1999








dates = input().split()
maxx = -1
p = -1
for date in dates:
    d,m,y = list(map(int,date.split("/")))
    if (1<=d<=31 )and (1<=m<=12) and y>0:
        cur = d + (m*30) + y* 365
        if cur > maxx:
            maxx = cur
            p = str(d).zfill(2)+"/"+str(m).zfill(2)+"/"+str(y).zfill(4)
print(p)