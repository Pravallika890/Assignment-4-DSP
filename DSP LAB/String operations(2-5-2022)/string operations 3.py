Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="data science with python"
>>> print(name)
data science with python
>>> print("name=",name)
name= data science with python
>>> print(name[5])
s
>>> print(name[10])
c
>>> print(name[5:-10])
science w
>>> print(name[0:16])
data science wit
>>> print(name[-2:-17])

>>> name.upper()
'DATA SCIENCE WITH PYTHON'
>>> name.lower()
'data science with python'
>>> name.isupper()
False
>>> name.islower()
True
>>> name.title()
'Data Science With Python'
>>> 'Data Science With Python'
'Data Science With Python'
>>> m="pravallika
SyntaxError: EOL while scanning string literal
>>> m="pravallika"
>>> g="bhulekhya"
>>> print(m+g)
pravallikabhulekhya
>>> l="prakhya"
>>> print(l)
prakhya
>>> print("c=",m+g)
c= pravallikabhulekhya
>>> print(c[5:-1])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(c[5:-1])
NameError: name 'c' is not defined
>>> c="pravallikabhulekhya"
>>> print(c[0:7])
pravall
>>> print(c[6:12])
likabh
>>> c.instr("ka")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c.instr("ka")
AttributeError: 'str' object has no attribute 'instr'
>>> c.in string("ka")
SyntaxError: invalid syntax
>>> c.instring("ka")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c.instring("ka")
AttributeError: 'str' object has no attribute 'instring'
>>> 
