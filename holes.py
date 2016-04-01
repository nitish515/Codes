a=raw_input('')
test=int(a)
n=test
namelist=list()
while test!=0:
    e=raw_input()
    namelist.append(e)
    test-=1
l=0
while n!=0:
    b=namelist[l]
    k=len(b)-1
    x=0
    while k!=-1:
        if b[k]=='A'or b[k]=='D'or b[k]=='O'or b[k]=='P'or b[k]=='R':
            x+=1
        elif b[k]=='B':
            x+=2
        k-=1
    n-=1
    l+=1
    print x