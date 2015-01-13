"""
Project Requirements

+  Have a hard-coded upper line, n.
+  Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
*  Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
*  Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
*  Each number should be printed on a new line.
"""

n = 100

print "Fizz buzz counting up to {0}".format(n)

for num in range(1,n):
  if ( num % 3 == 0 ) and ( num % 5 == 0 ):
    print "fizzbuzz"
  elif ( num % 3 == 0 ):
    print "fizz"
  elif ( num % 5 == 0 ):
    print "buzz"
  else:
    print "{0}".format(num)
