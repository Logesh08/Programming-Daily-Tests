R,C=map(int,input().split())
matrix=[list(map(int,input().split())) for row in range(R)]
maxSum=sum(matrix[0])
for row in matrix:
    maxSum=max(maxSum,sum(row))
for row in matrix:
    if sum(row)==maxSum:
        maxSum=-1
    else:
        print(*row)