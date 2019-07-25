Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LIST DATA TYPE

#If we want to represent a group of values as a single entity where insertionm order required to preserve and duplicate are allowed then we should go for
#list data type.#

#different type of data are allowed
#dupicated are allowed
#values should be enclosed within squre brackets.

>>> L1=[10,20,30,40,50,60]
>>> dir(L1)
[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(L1)
<class 'list'>
>>> 
>>> #APPEND
>>> help(L1.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> L1.append("200")
>>> L1
[10, 20, 30, 40, 50, 60, '200']
>>> 
>>> 
>>> #CLEAR
>>> help(L1.clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.

>>> L1.clear()
>>> L1
[]
>>> L1=[10,20,30,40,50,60]
>>> 
>>> #COPY
>>> help(L1.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> L1.copy()
[10, 20, 30, 40, 50, 60]
>>> 
>>> 
>>> #COUNT
>>> help(L1.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> L1.count(10)
1
>>> L2=[10,60,60,60]
>>> L2.count(60)
3
>>> 
>>> #EXTEND
>>> help(L1.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> L1.extend(L2)
>>> L1
[10, 20, 30, 40, 50, 60, 10, 60, 60, 60]
>>> L1=[10,20,30,40,50,60]
>>> 
>>> #INDEX
>>> help(L1.index)
Help on built-in function index:

index(value, start=0, stop=2147483647, /) method of builtins.list instance
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> L1.index(50)
4
>>> L1.index(10)
0
>>> 
>>> #INSERT
>>> help(L1.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> L1.insert(0,"12")
>>> L1
['12', 10, 20, 30, 40, 50, 60]
>>> 
>>> #POP
>>> help(L1.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> #remove the data in index
>>> L1.pop(0)
'12'
>>> L1
[10, 20, 30, 40, 50, 60]
>>> 
>>> 
>>> #REVERSE
>>> help(L1.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> L1.reverse()
>>> L1
[60, 50, 40, 30, 20, 10]
>>> 
>>> 
>>> #SORT
>>> help(L1.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Stable sort *IN PLACE*.

>>> L2=['krsihna','shivani','nayak','sahoo']
>>> L2.sort()
>>> L2
['krsihna', 'nayak', 'sahoo', 'shivani']
>>> 
