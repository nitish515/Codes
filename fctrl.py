def fctrl(num):
 count=0
 n=15
 while n!=0:
        count=count+(num/(5**n))
	n=n-1
 print count
a=raw_input('')
test=int(a)
numlist=list()
while test!=0:
        x=raw_input('')
	y=int(x)	
	numlist.append(y)
	test-=1
b=len(numlist)
l=0
while b!=0:
    fctrl(numlist[l])
    l+=1
    b-=1   