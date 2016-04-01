a = raw_input('')
e=a.split()
k=long(e[1])
test=long(e[0])
n=test
numlist=list()
while n!=0:
    x=raw_input('')
    y=long(x)
    numlist.append(y)
    n-=1
l=0
i=0
while test!=0:
    if numlist[l]%k==0:
        i+=1
    l+=1
    test-=1
print i

