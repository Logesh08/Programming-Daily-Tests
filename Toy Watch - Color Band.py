# Toy Watch - Color Band
# In a toy watch(12-hr format), there are N bands of different colors representing the time slots in 60 minutes. The program must accept N integers representing the duration of the N slots and a time T(12-hr format) as the input. The program must print the position of the band in which the minute hand is present at the time T. Then the program must print the starting time and the ending time of that band with respect to the given time T as the output. If the given time T is present in the middle of two bands, then the program must print -1 as the output.
# Note: The first band always starts from 0.

# Boundary Condition(s):
# 2 <= N <= 30

# Input Format:
# The first line contains N.
# The second line contains N integers separated by a space.
# The third line contains T.

# Output Format:
# The first line contains -1 or the position of the band followed by its starting time and ending time.

# Example Input/Output 1:
# Input:
# 6
# 10 10 10 10 10 10
# 04:15

# Output:
# 2 04:10 04:20

# Explanation:
# There are 6 bands in the toy watch.
# Band 1 -> 0 to 10 (0 is common for the bands 1 and 6)
# Band 2 -> 10 to 20 (10 is common for the bands 1 and 2)
# Band 3 -> 20 to 30 (20 is common for the bands 2 and 3)
# Band 4 -> 30 to 40 (30 is common for the bands 3 and 4)
# Band 5 -> 40 to 50 (40 is common for the bands 4 and 5)
# Band 6 -> 50 to 0 (50 is common for the bands 5 and 6)
# At T = 04:15, the minute hand is present in the 2nd band.
# The starting time of the 2nd band is 04:10.
# The ending time of the 2nd band is 04:20.

# Example Input/Output 2:
# Input:
# 4
# 20 15 20 5
# 06:55

# Output:
# -1

# Explanation:
# There are 4 bands in the toy watch.
# Band 1 -> 0 to 20 (0 is common for the bands 1 and 4)
# Band 2 -> 20 to 35 (20 is common for the bands 1 and 2)
# Band 3 -> 35 to 55 (35 is common for the bands 2 and 3)
# Band 4 -> 55 to 0 (55 is common for the bands 3 and 4)
# At T = 06:55, the minute hand is present in the middle of the bands 3 and 4.
# So -1 is printed as the output.




n = int(input())
arr = list(map(int,input().split()))
hour , mint = input().split(":")
mint = int(mint)
cur = 0
ocur = []
band = 0
for i in arr:
    band +=1
    p = cur
    cur+=i
    # if cur == 60: cur = 0
    if mint>=p and mint <=cur:
        ocur.append([p,cur,band])
    # print(p,cur,band)

if len(ocur)==1:
    if(ocur[0][0])==60:
        ocur[0][0]=0
        hour=int(hour)
        hour += 1
        hour %= 12
        h1=str(hour).zfill(2)
    else:
        h1 = hour
    if(ocur[0][1])==60:
        ocur[0][1]=0
        hour=int(hour)
        hour += 1
        hour %= 12
        h2=str(hour).zfill(2)
    else:
        h2=hour
    if h2=="00": h2=="12"
    print(ocur[0][2],h1+":"+str(ocur[0][0]).zfill(2),h2+":"+str(ocur[0][1]).zfill(2))
else:
    print(-1)