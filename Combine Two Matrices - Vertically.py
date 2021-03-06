# Combine Two Matrices - Vertically
# The program must accept two integer matrices M1 and M2 are of equal size R*C as the input. The first column or the last column of M2 always occurs in M1. The program must combine the given two matrices vertically based on that common column. Finally, the program must print the combined matrix as the output. The sum of integers must be printed in the common part of the combined matrix.
# Note: There is always only one way to combine the given two matrices.

# Boundary Condition(s):
# 2 <= R, C <= 50
# 1 <= Matrix element value <= 1000

# Input Format:
# The first line contains R and C separated by a space.
# The next R lines from the 2nd line, each contains C integers separated by a space representing the matrix M1.
# The next R lines from the R+2nd line, each contains C integers separated by a space representing the matrix M2.

# Output Format:
# The first R lines contain the integer values representing the combined matrix.

# Example Input/Output 1:
# Input:
# 6 4
# 7 6 5 9
# 1 2 1 1
# 2 3 5 8
# 1 1 7 5
# 7 3 7 9
# 5 3 8 9
# 8 2 4 6
# 6 3 2 2
# 9 6 5 3
# 5 1 2 1
# 7 7 4 3
# 7 5 6 3

# Output:
# 8 2 11 12 5 9
# 6 3 3 4 1 1
# 9 6 7 6 5 8
# 5 1 3 2 7 5
# 7 7 11 6 7 9
# 7 5 11 6 8 9

# Explanation:
# The last column of M2 occurs in the 2nd column of M1.
# The given matrices are combined based on the 2nd column of M1.

# Example Input/Output 2:
# Input:
# 3 4
# 92 75 40 18
# 19 53 20 64
# 90 74 10 32
# 40 38 49 73
# 20 49 43 55
# 10 38 26 74

# Output:
# 92 75 80 56 49 73
# 19 53 40 113 43 55
# 90 74 20 70 26 74




r,c=map(int,input().split()) 
m1=[list(map(int,input().split())) for i in range(r)]
m2=[list(map(int,input().split())) for i in range(r)]  
r1=[list(i) for i in zip(*m1)] 
r2=[list(i) for i in zip(*m2)]
res=[] 
for i in range(c): 
    if r2[i] in r1:  
        j=i
        k=r1.index(r2[i]) 
        break  
     
x,y=k,j 

if y>x: 
    res+=r2
    k=y-x
    for j in range(c):  
        if k>=len(res):  
          res.append(r1[j]) 
        else: 
          for u in range(r): 
            res[k][u]+=r1[j][u]
        k+=1
        
else: 
    res+=r1 
    k=x-y 
    
    for j in range(c): 
      if k>=len(res): 
        res.append(r2[j])
      else: 
        for u in range(r): 
          res[k][u]+=r2[j][u] 
      k+=1 
      
  
for i in zip(*res): 
    print(*i)