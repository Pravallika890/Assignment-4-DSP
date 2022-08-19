Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="hello"
>>> print(a)
hello
>>> float a=10.4;
SyntaxError: invalid syntax
>>> a=10.4
>>> type(a)
<class 'float'>
>>> int("123")
123
>>> float("123")
123.0
>>> a=10
>>> b=30
>>> a+b
40
>>> a-b
-20
>>> a/b
0.3333333333333333
>>> a%b
10
>>> p=23
>>> type(p)
<class 'int'>
>>> a=0123
SyntaxError: invalid token
>>> s="Pravallika"
>>> type(s)
<class 'str'>
>>> a=25
>>> b=30
>>> a,b
(25, 30)
>>> a,b=b,a
>>> print(a,b)
30 25
>>> a=30
>>> b=40
>>> c=a>b
>>> type(c)
<class 'bool'>
>>> a=prakhya143
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a=prakhya143
NameError: name 'prakhya143' is not defined
>>> a=10
>>> b=20
>>> a==b
False
>>> a,b=b,a
>>> a=10
>>> b=3=
SyntaxError: invalid syntax
>>> a=10
>>> b=30
>>> a,b=b,a
>>> print(a,b)
30 10
>>> a=temp
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a=temp
NameError: name 'temp' is not defined
>>> a=4
>>> b=2
>>> a=c
>>> c=b
>>> print(a,b)
False 2
>>> a=10
>>> b=20
>>> c=a
>>> a=b
>>> b=c
>>> print(a,b)
20 10
>>> 
