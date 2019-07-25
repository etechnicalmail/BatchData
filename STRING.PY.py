Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #STRING
>>> 
>>> s1="krishna"
>>> type(s1)
<class 'str'>
>>> 
>>> dir(s1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> #CAPITALIZE
>>> help s1.capitalize()
SyntaxError: invalid syntax
>>> help(s1.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> s1.capitalize()
'Krishna'
>>> 
>>> #CASEFOLD
>>> help(s1.casefold)
Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.

>>> s2="hi,there are for me"
>>> s2.casefold()
'hi,there are for me'
>>> s2="Hi,There are for me"
>>> s2.casefold()
'hi,there are for me'
>>> 
>>> #CENTER
>>> help(s1.center)
Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> s1.center(10)
' krishna  '
>>> s1.center(100)
'                                              krishna                                               '
>>> #space are count here.
>>> 
>>> #COUNT
>>> help(s2.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> s2="Hi,There are for me"
>>> s2.count("are")
1
>>> # kete thara use heichi " are"
>>> 
>>> #ENCODE
>>> help(s2.encode)
Help on built-in function encode:

encode(encoding='utf-8', errors='strict') method of builtins.str instance
    Encode the string using the codec registered for encoding.
    
    encoding
      The encoding in which to encode the string.
    errors
      The error handling scheme to use for encoding errors.
      The default is 'strict' meaning that encoding errors raise a
      UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
      'xmlcharrefreplace' as well as any other name registered with
      codecs.register_error that can handle UnicodeEncodeErrors.

>>> s2="Hi,There are for me"
>>> s2.encode()
b'Hi,There are for me'
>>> s2="Hi,There are for & me"
>>> s2.encode()
b'Hi,There are for & me'
>>> # convert into a coded form
>>> 
>>> #ENDSWITH
>>> help(s2.endswith)
Help on built-in function endswith:

endswith(...) method of builtins.str instance
    S.endswith(suffix[, start[, end]]) -> bool
    
    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.

>>> s2="Hi,There are for me"
>>> s2.endswith("for me")
True
>>> #The endswith() method returns True if the string ends with the specified value, otherwise False.
>>> 
>>> #EXPANDTABS
>>> help(s2.expandtabs)
Help on built-in function expandtabs:

expandtabs(tabsize=8) method of builtins.str instance
    Return a copy where all tab characters are expanded using spaces.
    
    If tabsize is not given, a tab size of 8 characters is assumed.

>>> s2="Hi,There are for me"
>>> s2.expandtabs(2)
'Hi,There are for me'
>>> s2="Hi\t,There \tare \tfor \tme"
>>> s2.expanstabs(7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s2.expanstabs(7)
AttributeError: 'str' object has no attribute 'expanstabs'
>>> s2.expandtabs(7)
'Hi     ,There        are    for    me'
>>> #The expandtabsize() method sets the tab size to the specified number of whitespaces and " using in string \t"
>>> 
>>> # FIND
>>> help(s2.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> s2="Hi,There are for me"
>>> s2.find("for")
13
>>> #
KeyboardInterrupt
>>> #'The find() method finds the first occurrence of the specified value.

#The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below
>>> 
>>> #FORMAT
>>> s2="Hi,There are for me"
>>> s2="Hi,There {are} for me"
>>> s2.format(are=r)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s2.format(are=r)
NameError: name 'r' is not defined
>>> s2.format(are='r')
'Hi,There r for me'
>>> #Help: The format() method formats the specified value(s) and insert them inside the string's placeholder.

#The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

#The format() method returns the formatted string.
>>> 
>>> #INDEX
>>> s2="Hi,There are for me"
>>> s2.index("are")
9
>>> # Help: The index() method finds the first occurrence of the specified value.

#The index() method raises an exception if the value is not found.

#The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
>>> 
>>> #ISALNUM
>>> s2="Hi,There are for me"
>>> s2.isalnum()
False
>>> s2="Hi,There are for me23"
>>> s2.isalnum()
False
>>> #help: The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

#Example of characters that are not alphanumeric: (space)!#%&? etc.
>>> 
>>> #ISALPHA
>>> s2="hi,there are for me"
>>> s2.isalpha()
False
>>> s3="hi"
>>> s3.isalpha()
True
>>> # help:The isalpha() method returns True if all the characters are alphabet letters (a-z).

#Example of characters that are not alphabet letters: (space)!#%&? etc.
>>> 
>>> #ISDECIMAL
>>> '''The isdecimal() method returns True if all the characters are decimals (0-9)'''
'The isdecimal() method returns True if all the characters are decimals (0-9)'
>>> 
>>> #ISDIGIT
>>> '''The isdigit() method returns True if all the characters are digits, otherwise False'''
'The isdigit() method returns True if all the characters are digits, otherwise False'
>>> 
>>> #ISIDENTIFIER
>>> '''The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.'''
'The isidentifier() method returns True if the string is a valid identifier, otherwise False.\n\nA string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.'
>>> 
>>> 
>>> #ISLOWER
>>> '''The islower() method returns True if all the characters are in lower case, otherwise False.'''
'The islower() method returns True if all the characters are in lower case, otherwise False.'
>>> 
>>> #ISNUMERIC
>>> '''The isumeric() method returns True if all the characters are numeric (0-9), otherwise False'''
'The isumeric() method returns True if all the characters are numeric (0-9), otherwise False'
>>> 
>>> #ISPRINTABLE
>>> '''The isprintable() method returns True if all the characters are printable, otherwise Fals'''
'The isprintable() method returns True if all the characters are printable, otherwise Fals'
>>> 
>>> #ISSPACE
>>> '''The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.'''
'The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.'
>>> 
>>> #ISTITTLE
>>> '''
KeyboardInterrupt
>>> '''The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False'''
'The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False'
>>> 
>>> #ISUPPER
>>> '''The isupper() method returns True if all the characters are in upper case, otherwise False'''
'The isupper() method returns True if all the characters are in upper case, otherwise False'
>>> 
>>> 
>>> #JOIN
>>> SS=("John", "Peter", "Vicky")
>>> T="%".join(SS)
>>> T
'John%Peter%Vicky'
>>> 
>>> #help: The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.
>>> # SYNTAX:string.join(iterable)
>>> 
>>> #LOWER
>>> ss="Hello MY frnds"
>>> ss.lower()
'hello my frnds'
>>> #help: The lower() method returns a string where all characters are lower case.
>>> 
>>> #PARTITION
>>> ss=" I could eat bananas all days"
>>> ss.partitiob
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    ss.partitiob
AttributeError: 'str' object has no attribute 'partitiob'
>>> ss.partition("bananas")
(' I could eat ', 'bananas', ' all days')
>>> #help: The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
>>> 
>>> 
