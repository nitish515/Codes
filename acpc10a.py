def progr(a,b,c):
    if a-b==b-c:
        k=b-a
        e=k+c
        return "AP %d"%e
    elif b/a==c/b:
        k=b/a
        e=c*k
        return "GP %d"%e        
count=0
pro=list()
while True:
    x=raw_input('')
    y=x.split()
    if y[0]==y[1] and y[0]=='0':
        break
    else:
        pro.append(x)
        count+=1
b=0
while count!=0:
    num=pro[b].split()
    print progr(int(num[0]),int(num[1]),int(num[2]))
    b+=1
    count-=1