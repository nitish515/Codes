a = raw_input('')
k=long(a)
n=k
numlist=list()
while n!=0:
    x=raw_input('')
    y=int(x)
    numlist.append(y)
    n-=1
l=0
i=0
while k!=0:
    while numlist[l]!=0:
        if numlist[l]!=1:
            if numlist[l]%(numlist[l]-1)==0:
                numlist[l]=numlist[l]-(numlist[l]-1)
                i+=1
            else: numlist[l]-=1
        else: numlist[l]-=1
    if i%2==0:
        print "BOB"
    else: print "ALICE"
    k-=1
    l+=1    
