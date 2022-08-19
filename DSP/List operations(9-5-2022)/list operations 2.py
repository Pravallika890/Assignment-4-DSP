Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p=["1","pravallika","2.45","aq2"]
>>> print(p)
['1', 'pravallika', '2.45', 'aq2']
>>> l=[1,2,3,4]
>>> l=l+[7,8,9]
>>> print(l)
[1, 2, 3, 4, 7, 8, 9]
>>> l.max()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l.max()
AttributeError: 'list' object has no attribute 'max'
>>> l max()
SyntaxError: invalid syntax
>>> l_max()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l_max()
NameError: name 'l_max' is not defined
>>> i=[10,20,30]
>>> max(i)
30
>>> min(p)
'1'
>>> min(i)
10
>>> l=["mango","banana","mango"]
>>> max(l)
'mango'
>>> min(l)
'banana'
>>> len(l)
3
>>> a=[10,30,50,2]
>>> a.sort()
>>> print(a)
[2, 10, 30, 50]
>>> a=["p","a","q"]
>>> a.sort()
>>> print(a)
['a', 'p', 'q']
>>> 
