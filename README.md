
## Python provides several ways to find what functions/methods a dictionary has.

### 1. dir() — see all available methods

my_dict = {"name": "Manjeet", "age": 30}
print(dir(my_dict))

You’ll get something like:
`
['__class__', '__contains__', '__delitem__',
 '__getitem__', '__iter__', ...
 'clear', 'copy', 'fromkeys',
 'get', 'items', 'keys', 'pop',
 'popitem', 'setdefault', 'update', 'values']
`
The methods without __ are the ones you’ll use most often:

clear()
copy()
fromkeys()
get()
items()
keys()
pop()
popitem()
setdefault()
update()
values()
`

### 2. Get only the “normal” methods

You can filter out the special __xxx__ methods:

methods = [x for x in dir(my_dict) if not x.startswith("__")]
print(methods)

Output:

['clear', 'copy', 'fromkeys', 'get', 'items',
 'keys', 'pop', 'popitem', 'setdefault',
 'update', 'values']

This is a very useful trick for learning Python.


### 3. Check what a particular method does

Use help():

help(my_dict.get)

Or:

help(dict.get)

You’ll see documentation explaining how get() works.

For example:

my_dict = {"name": "Manjeet"}
print(my_dict.get("name"))

Output:

Manjeet

And unlike:

my_dict["age"]

get() can safely handle a missing key:

print(my_dict.get("age"))

Output:

None

You can also provide a default:

print(my_dict.get("age", 0))

Output: 0

### 4. type() tells you what object you have

my_dict = {"name": "Manjeet"}
print(type(my_dict))

Output:

<class 'dict'>

Then you can do:

help(dict)

This is actually a great way to learn Python built-in types.

For example:

help(list)
help(dict)
help(set)
help(tuple)
help(str)

And:

dir(list)
dir(dict)
dir(set)
dir(tuple)
dir(str)

Very useful learning pattern

Whenever you encounter a Python object:

object = ...

Try:

type(object)   # What is it?
dir(object)    # What can I do with it?
help(object)   # How does it work?

For example:

numbers = [1, 2, 3]
print(type(numbers))
print([x for x in dir(numbers) if not x.startswith("__")])

This lets you discover Python yourself instead of memorizing every method.


### Other useful functions in python 


*map()

Transform every item

Many → Many

*filter()

Select items

Many → Fewer

*reduce()

Combine items

Many → One

*zip()

Combine iterables

Multiple → Tuples

*enumerate()

Index + value

Index + Value

*any()

At least one is true

Boolean

*all()

Everything is true

Boolean

*sorted()

Sort items

Sorted iterable