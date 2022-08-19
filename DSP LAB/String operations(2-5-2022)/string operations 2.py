Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="pravallika"
>>> s.isascii()
True
>>> s="\n"
>>> s.isascii()
True
>>> s="/u00f8"
>>> s.isascii()
True
>>> s.isdigit()
False
>>> s="Pravallika"
>>> s.islower()
False
>>> s="Pravallika"
>>> s.isupper()
False
>>> s.upper()
'PRAVALLIKA'
>>> a="mudavarthi pravallika"
>>> a.isspace()
False
>>> a="p r a v a l l i k a"
>>> a.isspace()
False
>>> a=" "
>>> a.isspace()
True
>>> a.istitle()
False
>>> a="Mudavarthi Pravallika"
>>> a.istitle()
True
>>> a="rajiv gandhi "
>>> a.title()
'Rajiv Gandhi '
>>> p="anvika
SyntaxError: EOL while scanning string literal
>>> p="anvika"
>>> p.swapcase()
'ANVIKA'
>>> s="PRAVALLIKA"
>>> s.swapcase()
'pravallika'
>>> a="roses are red"
>>> a.pratition("are")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pratition("are")
AttributeError: 'str' object has no attribute 'pratition'
>>> a.partition("are")
('roses ', 'are', ' red')
>>> 
