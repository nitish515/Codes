def computepay(hrs,rate):
  hrs = float(a)  
  rate = float(b)
  pay = hrs*rate
  if hrs > 40:
    pay = pay*1.5
    print pay
  else:
    print pay
x = raw_input("Enter Hours: ")
try:
 a = float(x)
 y = raw_input("Enter Rate: ")
 b = float(y)
 computepay(a,b)
except:
 print 'Error, please enter numeric input'
