# Sort N Dates
# N dates are passed as the input to the program. The date consists of the day of the month DD, the month MMM and the year YYYY. The day, the month and the year can be in any order separated by a hyphen. The program must sort the N dates and print them as the output.
# Note: MMM will be like Jan, Feb, Mar,.... till Dec in mixed case.

# Boundary Condition(s):
# 1 <= N <= 20
# 1 <= DD <= 31
# 1 <= YYYY <= 9999

# Input Format:
# The first line contains N.
# The next N lines, each containing a date.

# Output Format:
# The first N lines contain the sorted dates in DD-MMM-YYYY format.

# Example Input/Output 1:
# Input:
# 4
# 12-Mar-2021
# Mar-18-1999
# 2015-Apr-30
# 2012-11-Sep

# Output:
# 18-Mar-1999
# 11-Sep-2012
# 30-Apr-2015
# 12-Mar-2021

# Explanation:
# The given dates are sorted in ascending order.

# Example Input/Output 2:
# Input:
# 2
# 12-MAR-2021
# Mar-12-2021

# Output:
# 12-MAR-2021
# 12-Mar-2021












n=int(input())
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
arr = []
for _ in range(n):
    l = sorted(input().strip().split('-'),key=len)
    arr.append(l)
arr = sorted(arr,key = lambda x: (int(x[2]),months.index(x[1].lower()),int(x[0])))

for l in arr:
    print(*l,sep='-')