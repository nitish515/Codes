a=raw_input('')
e=a.split()
k=int(e[0])
x=float(e[1])
if k%5==0 and 0.5<=x-k:
    x=x-k-0.5
print x