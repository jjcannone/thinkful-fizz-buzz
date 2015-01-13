import sys
"""
Project Requirements

+  Have a hard-coded upper line, n.
+  Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
+  Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
+  Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
+  Each number should be printed on a new line.

+  If the user supplies a value at the command line when script runs, we'll use that value.
+  Otherwise, we'll use the raw_input() function to get a value from the user.
"""

n = 0

while n < 2:
  try:
    n = int(sys.argv[1]) if int(sys.argv[1]) > 1 else 2
  except (IndexError, ValueError):
    try:
      n = int(raw_input("Enter the FizzBuzz limit (an integer greater than 1): "))
    except ValueError:
      print "Invalid input... Please enter an integer greater than 1."

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
