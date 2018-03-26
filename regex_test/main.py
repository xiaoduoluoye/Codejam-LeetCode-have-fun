from regex import *

print (f('a*b', 'acb'))
print (f('abc*', 'abbc'))
print (f('**bc', 'bc'))
print ('\n')
print (f('a**b', 'acb'))
print (f('abc*', 'abbcabcdd'))
print (f('*bc', 'bcd'))
