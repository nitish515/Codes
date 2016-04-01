a=raw_input('')
test=int(a)
n=test
k=test
numlist=list()
while test!=0:
    e=raw_input()
    y=int(e)
    numlist.append(y)
    test-=1
print numlist
while n!=0:
    l=0
    while k-1!=0:
        if numlist[l]>numlist[l+1]:
            x=numlist[l]
            numlist[l]=numlist[l+1]
            numlist[l+1]=x
        k-=1
        l+=1
    n-=1
i=0
while len(numlist)!=0:
    print numlist[i]
    del numlist[i]