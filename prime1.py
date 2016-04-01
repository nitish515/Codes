import math
def prime(m,n):
 while m<=n:
    count=0
    x=2
    while x<=m:
        if m%x==0:
            count=count+1
        x=x+1
    if count==1:
        print m 
    m=m+1 		
k=raw_input('')
test = int (k)
while test!=0:
    l=raw_input('')
    num=l.split()
    a=int(num[0])
    b=int(num[1])
    prime(a,b)
    print "\n"	
    test=test-1