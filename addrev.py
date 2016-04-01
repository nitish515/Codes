def rev(n):
        i=n
        count=-1
	k=0
	while n!=0:
	    n=n/10
	    count+=1
	while i!=0:    
		k=k+((i%10)*(10**count))
		i=i/10
		count-=1
	return k
a=raw_input('')
test=int(a)
numlist=list()
while test!=0:
        x=raw_input('')	
	numlist.append(x)
	test-=1
b=len(numlist)
l=0
while b!=0:
    num=numlist[l].split()
    a=int(num[0])
    x=int(num[1])
    print rev(rev(a)+rev(x))
    l+=1
    b-=1   

