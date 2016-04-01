def computegrade(scr): 
  if scr > 0.0 and scr < 1.0:
     if scr >= 0.9:
        return "A"
     elif scr >= 0.8:
	    return "B"
     elif scr >= 0.7:
        return "C"
     elif scr >= 0.6:
        return "D"
     else:
	    return "F"
  else:
     return "Bad Score"
a = raw_input("Enter Score: ")
try:
 x = float(a)
 y=computegrade(x)
 print y
except:
 print "Bad Score"	