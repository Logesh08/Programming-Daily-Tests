# Find Total Race Time
# There are N laps in a car race. For each lap, the program must accept the lap time(in seconds) in 8-bit binary format as the input. The program must find the total race time and print it in the format of HH:MM:SS as the output.

# Boundary Condition(s):
# 2 <= N <= 100

# Input Format:
# The first line contains N.
# The next N lines, each contains the lap time(in seconds) in 8-bit binary format.

# Output Format:
# The first line contains the total race time in the format of HH:MM:SS.

# Example Input/Output 1:
# Input:
# 3
# 00111000
# 01001111
# 01000100

# Output:
# 00:03:23

# Explanation:
# 1st lap: 00111000 -> 56 seconds.
# 2nd lap: 01001111 -> 79 seconds.
# 3rd lap: 01000100 -> 68 seconds.
# So the total time is 203 seconds.
# Hence the output is 00:03:23.

# Example Input/Output 2:
# Input:
# 6
# 01110001
# 10001100
# 10111100
# 11010100
# 10101001
# 10001100

# Output:
# 00:16:02



n=int(input())
secs=0
for _ in range(n):
    i=input().strip()
    secs+=(int(i,2))
    
seconds=secs%(24*3600)
hour=seconds//3600
seconds%=3600
mins = seconds//60
seconds%=60
print("%02d:%02d:%02d"%(hour,mins,seconds))
