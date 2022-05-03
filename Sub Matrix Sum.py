## Method 1
s,r,c=map(int,input().split())
li=[[int(i) for i in input().split()] for j in range(r)]
q=0
for i in range(r):
    for j in range(c):
        for a in range(i,r):
            for b in range(j,c):
                x=[]
                p=0
                for d in range(i,a+1):
                    y=[]
                    for e in range(j,b+1):
                        y.append(li[d][e])
                        p+=li[d][e]
                    x.append(y)
                if p==s:
                    if q==1:
                        print("END")
                    for f in x:
                        print(*f)
                    q=1