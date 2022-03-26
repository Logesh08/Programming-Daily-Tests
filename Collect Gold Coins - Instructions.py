r,c=map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
s= input().strip()
x,y = 0,0
visited[0][0]= mat[0][0]
coins = mat[0][0]
mat[0][0]=0
for C in s:
    if C == 'N' and x>0:
        x-=1
    elif C== 'S' and x<r-1:
        x+=1
    elif C== 'E' and y<c-1:
        y+=1
    elif C== 'W' and y>0:
        y-=1
    
    if visited[x][y]=='*':
        pass
    elif visited[x][y]!=0:
        visited[x][y]-=1
        coins-=1
        mat[x][y]+=1
        if visited[x][y]==0:
            visited[x][y]='*'
    else:
        visited[x][y]=mat[x][y]
        coins+=mat[x][y]
        mat[x][y]=0
print(coins)