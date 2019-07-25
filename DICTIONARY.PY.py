Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DICTIONARY
>>> 
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> type(d1)
<class 'dict'>
>>> 
>>> dir(d1)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> #CLEAR
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.clear()
>>> d1
{}
>>> #help: The clear() method removes all the elements from a dictionary.
>>> 
>>> #COPY
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.copy()
{'a': 'qwerty', 'b': 'ford', 'c': 'yes'}
>>> #help: The copy() method returns a copy of the specified dictionary.


>>> #FROMKEYS
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> x=('key1','key2','key3')
>>> y=
SyntaxError: invalid syntax
>>> y=(1,2,3)
>>> xy=dict.fromkeys(x,y)
>>> print(xy)
{'key1': (1, 2, 3), 'key2': (1, 2, 3), 'key3': (1, 2, 3)}
>>> x=('key1','key2','key3')
>>> x.fromkeys(x)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x.fromkeys(x)
AttributeError: 'tuple' object has no attribute 'fromkeys'
>>> 
>>> 
>>> #help: The fromkeys() method returns a dictionary with the specified keys and values.
>>> 
>>> 
>>> 
>>> 
>>> #GET
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.get("a")
'qwerty'
>>> d1.get("a","c")
'qwerty'
>>> d1.get("d","hello")
'hello'
>>> 
>>> #help: The get() method returns the value of the item with the specified key
>>> 
>>> 
>>> #ITEMS
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.items()
dict_items([('a', 'qwerty'), ('b', 'ford'), ('c', 'yes')])
>>> 
>>> # help: The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes done to the dictionary,
>>> 
>>> 
>>> #KEYS
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.keys()
dict_keys(['a', 'b', 'c'])
>>> 
>>> #help: The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.The view object will reflect any changes done to the dictionary.
>>> 
>>> #POP
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.pop("b")
'ford'
>>> d1
{'a': 'qwerty', 'c': 'yes'}
>>> #help:The pop() method removes the specified item from the dictionary.The value of the removed item is the return value of the pop() method
>>> 
>>> 
>>> #POPITEM
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.popitem()
('c', 'yes')
>>> d1
{'a': 'qwerty', 'b': 'ford'}
>>> # help:The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.The removed item is the return value of the popitem() method, as a tuple,
>>> 
>>> 
>>> #SETDEFAULT
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.setdefault("a","mula")
'qwerty'
>>> d1
{'a': 'qwerty', 'b': 'ford', 'c': 'yes'}
>>> #help:The setdefault() method returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value
>>> 
>>> 
>>> #UPDATE
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.update("d)
	  
SyntaxError: EOL while scanning string literal
>>> d1.update("d":"white")
SyntaxError: invalid syntax
>>> d1.update({"d":"white"})
>>> d1
{'a': 'qwerty', 'b': 'ford', 'c': 'yes', 'd': 'white'}
>>> 
>>> #help:The update() method inserts the specified items to the dictionary.The specified items can be a dictionary, or an iterable object.
>>> 
>>> 
>>> #VALUES
>>> d1={"a":"qwerty","b":"ford","c":"yes"}
>>> d1.values()
dict_values(['qwerty', 'ford', 'yes'])
>>> 
>>> #help:
KeyboardInterrupt
>>> #help:The values() method returns a view object. The view object contains the values of the dictionary, as a list.The view object will reflect any changes done to the dictionary
>>> 
