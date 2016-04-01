total=0
count=0
avg=0
while True:
 a=raw_input("Enter Number: ")
 if a=='done':
    break 
 else:
    try: 
           #num=int(a)
	   total=total+int(a)
	   count=count+1
	   avg=float(total)/count
    except:
       print 'invalid input'
	   
print total," ",count," ",avg