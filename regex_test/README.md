Simply regex parser:
to do this:
f('a*b', 'acb') => True
f('abc*', 'abbc') => False
f('**bc', 'bc') => True


Test Result:
print (f('a*b', 'acb'))
print (f('abc*', 'abbc'))
print (f('**bc', 'bc'))
print ('\n')
print (f('a**b', 'acb'))
print (f('abc*', 'abbcabcdd'))
print (f('*bc', 'bcd'))

True
False
True


False
True
True
