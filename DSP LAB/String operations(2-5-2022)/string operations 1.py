Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="everything happens for a reason"
>>> s.capitalize()
'Everything happens for a reason'
>>> s.isalpha()
False
>>> s.isdigit()
False
>>> s.count(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.count(a)
NameError: name 'a' is not defined
>>> count=s.count("for")
>>> print(count)
1
>>> s.islower()
True
>>> s.isupper()
False
>>> s.isspace()
False
>>> s.istitle()
False
>>> s.upper()
'EVERYTHING HAPPENS FOR A REASON'
>>> s.lower()
'everything happens for a reason'
>>> s.partition("happens")
('everything ', 'happens', ' for a reason')
>>> s.replace("everything","anything")
'anything happens for a reason'
>>> s.split()
['everything', 'happens', 'for', 'a', 'reason']
>>> s.swapcase()
'EVERYTHING HAPPENS FOR A REASON'
>>> a="sri"
>>> b="nidhi"
>>> a.join(b)
'nsriisridsrihsrii'
>>> b.join(a)
'snidhirnidhii'
>>> 
