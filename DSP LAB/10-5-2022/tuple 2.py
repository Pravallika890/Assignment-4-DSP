Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=("a","b","c","d")
>>> a.count("c")
1
>>> v=(1,3,4,5)
>>> v.count(3)
1
>>> v[0]
1
>>> v[-3]
3
>>> v[0:3]
(1, 3, 4)
>>> v[ :-1]
(1, 3, 4)
>>> v.index(3)
1
>>> v[0:1:3]
(1,)
>>> t=(1,2,3)
>>> p=(4,5,6)
>>> t+p
(1, 2, 3, 4, 5, 6)
>>> t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> del p
>>> print(p)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(p)
NameError: name 'p' is not defined
>>> print(t)
(1, 2, 3)
>>> del t
>>> print(t)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(t)
NameError: name 't' is not defined
>>> s=("a","b","c")
>>> "a" in s
True
>>> c=(1,2,3,4)
>>> 1 in c
True
>>> 8 in c
False
>>> 
