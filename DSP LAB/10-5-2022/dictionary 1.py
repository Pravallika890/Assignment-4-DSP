Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d["name"]="pravallika"
>>> print(d)
{'name': 'pravallika'}
>>> d["roll no"]="s180890"
>>> print(d)
{'name': 'pravallika', 'roll no': 's180890'}
>>> len(d)
2
>>> d["roll no"]="890"
>>> print(d)
{'name': 'pravallika', 'roll no': '890'}
>>> d["class"]=2D
SyntaxError: invalid syntax
>>> d["class"]="2D"
>>> print(d)
{'name': 'pravallika', 'roll no': '890', 'class': '2D'}
>>> del (d["name"])
>>> print(d)
{'roll no': '890', 'class': '2D'}
>>> d.popitem()
('class', '2D')
>>> d.pop("roll no")
'890'
>>> print(d)
{}
>>> d=dict([(1,2),(3,4),(5,6)])
>>> print(d)
{1: 2, 3: 4, 5: 6}
>>> d.keys()
dict_keys([1, 3, 5])
>>> d.values()
dict_values([2, 4, 6])
>>> 
