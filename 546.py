# import re module
import re

Substring ='string'


String1 ='''We are learning regex with geeksforgeeks 
		regex is very useful for string matching.
		It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks 
		regex is very useful for string matching.
		It is fast too.'''

# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE)[0])
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))

# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))
