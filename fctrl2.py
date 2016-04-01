a=raw_input('')
test=int(a)
n=test
numlist=list()
while test!=0:
    e=raw_input()
    y=int(e)
    numlist.append(y)
    test-=1
l=0
while n!=0:
    k=numlist[l]
    x=1
    while k!=0:
         x*=k
         k-=1
    print x
    n-=1
    l+=1