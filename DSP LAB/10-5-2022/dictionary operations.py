Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d["name"]="pravallika"
>>> print(d)
{'name': 'pravallika'}
>>> d["roll no"]="s180890"
>>> print(d)
{'name': 'pravallika', 'roll no': 's180890'}
>>> d["class"]="CSE2D"
>>> print(d)
{'name': 'pravallika', 'roll no': 's180890', 'class': 'CSE2D'}
>>> d.key("name")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d.key("name")
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys()
dict_keys(['name', 'roll no', 'class'])
>>> d.get("name")
'pravallika'
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values(['pravallika', 's180890', 'CSE2D'])
>>> d.get("name")
'pravallika'
>>> d.clear()
>>> print(d)
{}
>>> a={10:5,6:3,4:2}
>>> n=a.copy()
>>> print(n)
{10: 5, 6: 3, 4: 2}
>>> print(a)
{10: 5, 6: 3, 4: 2}
>>> key={"a","e","i","o","u"}
>>> vowels=dict.fromkeys(key)
>>> print(vowel)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(vowel)
NameError: name 'vowel' is not defined
>>> print(vowels)
{'a': None, 'e': None, 'i': None, 'u': None, 'o': None}
>>> keys={"a","e","i","o","u"}
>>> values="vowel"
>>> vowels=dict.fromkeys(keys,values)
>>> print(vowels)
{'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'u': 'vowel', 'o': 'vowel'}
>>> vowels.items()
dict_items([('a', 'vowel'), ('e', 'vowel'), ('i', 'vowel'), ('u', 'vowel'), ('o', 'vowel')])
>>> vowels.pop("a")
'vowel'
>>> print(vowels)
{'e': 'vowel', 'i': 'vowel', 'u': 'vowel', 'o': 'vowel'}
>>> d={10:5,6:3,4:2}
>>> d.popitem()
(4, 2)
>>> print(d)
{10: 5, 6: 3}
>>> d1={8:4}
>>> d.update(d1)
>>> print(d)
{10: 5, 6: 3, 8: 4}
>>> 
