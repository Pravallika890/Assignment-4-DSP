Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={1,2,3,4}
>>> print(a)
{1, 2, 3, 4}
>>> type(a)
<class 'set'>
>>> help(s)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    help(s)
NameError: name 's' is not defined
>>> help(a)

>>> a.add(5)
>>> print(a)
{1, 2, 3, 4, 5}
>>> a.update([7,6,8])
>>> print(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> print(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.discard(5)
>>> print(a)
{1, 2, 3, 4, 6, 7, 8}
>>> a.discard(9)
>>> print(a)
{1, 2, 3, 4, 6, 7, 8}
>>> print(a)
{1, 2, 3, 4, 6, 7, 8}
>>> a.remove(6)
>>> print(a)
{1, 2, 3, 4, 7, 8}
>>> a.remove(9)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.remove(9)
KeyError: 9
>>> print(a)
{1, 2, 3, 4, 7, 8}
>>> a.pop()
1
>>> a.pop(7)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop(7)
TypeError: pop() takes no arguments (1 given)
>>> a.clear()
>>> print(a)
set()
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a&b
{4, 5}
>>> a.intersection(b)
{4, 5}
>>> b.intersection(a)
{4, 5}
>>> 
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a-b
{1, 2, 3}
>>> a.difference(b)
{1, 2, 3}
>>> b-a
{8, 6, 7}
>>> a^b
{1, 2, 3, 6, 7, 8}
>>> 
