import sys
print('Checking syntax of', sys.argv[1])
from ast import parse
try:
    parse(open(sys.argv[1]).read())
    print('Syntax is valid')
except SyntaxError as e:
    print('Syntax error:', e)
