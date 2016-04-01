def nsteps(a,b):
    if a==b:
        if a%2!=0:
            return a*2-1
        else:
            return a*2
    elif a-b==2:
        if a%2!=0:
            return a+b-1
        else:
            return a+b
    else:
        return "No Number"    
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
    x=int(num[0])
    y=int(num[1])
    print nsteps(x,y)
    l+=1
    b-=1   