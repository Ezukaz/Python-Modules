*This project has been created as part of the 42 curriculum by katakaha.*

# Python Module 03

## Description

####

## What is Learnt from Each Assignment

1. **ex0 - Command-Line Input**
2. **ex1 - List**
3. **ex2 - Tuple**
4. **ex3 - Set and its Operator**
5. **ex4 - Dictionary**
6. **ex5 - Generator (yield)**
7. **ex6 - Comprehension**

## Resources

1. CLI<br>[[Python]コマンドライン引数を受け取る方法](https://qiita.com/to-fmak/items/4b136479099826959ea6)
    > **kataPoint:**<br>
    Arguments should always be processed with some form of input validation. If they are received in string form there is no need to validate as strings can handle all types of input.
2. List<br>[Python Lists](https://www.youtube.com/watch?v=spjE6cmV1Cs&list=PL8HmoRTjTSlEgS2GsFaDr9zDLC1xD9FZf&index=9)
    > **kataPoint:**<br>
    If you are to use the str args input, unless you are going to process them as strings you need to have input validation. Use try and except to catch any errors that might crash your program. Common errors include ValueError, TypeError, KeyError, and DivisionByZeroError might be worth considering if you are handling numbers.<br>
    Lists can be combined with the "+" sign.<br><br>
    Here are a few methods for lists:<br>
    .append(value)<br> .remove(first value)<br> .sort(key=None, reverse=False)<br> .pop(index or last if no index given)<br> .extend(iterable(you can add lists or tuples))<br> .insert(index, value)<br> .clear()<br> .index(value, start(optional index), end(optional index, not included)) Caution!!: returns ValueError if not found<br> .count(value)<br> .reverse()
3. Tuple<br>[Lists vs Tuples vs Sets](https://www.youtube.com/watch?v=11WrzU81q68&list=PL8HmoRTjTSlEgS2GsFaDr9zDLC1xD9FZf&index=12)<br>
[Python tupleの使い方](https://paiza.jp/works/reference/article-python-tuple)
    > **kataPoint:**<br>
    Using tuples as the key to a dictionary can be useful. There is no such thing as tuple comprehension but if it looks like it then it is tuple + generator expression. Generators use the "()" so that's how tuples got left out of comprehension. You can make a tuple comprehension by generators or just converting a list comprehension to a tuple.
4. Set<br>[Pythonのset（セット）とは？基本的な使い方や集合演算をわかりやすく解説](https://www.rstone-jp.com/column/145109/)
    > **kataPoint:**<br>
    Sets are very useful for making groups that have no duplicates. This means you can combine and filter.
    **Union |**: combines two sets together.
    **Difference -**: will get the difference of two sets by subtracting one from the other. Depending on the order you will get varied results.
    **Intersection &**: self explanatory
    **Symetrical diff^**: Gets all differences (opposite of intersection)
5. Dict<br>[Dictionaries](https://www.youtube.com/watch?v=4t10v2QmTHU&list=PL8HmoRTjTSlEgS2GsFaDr9zDLC1xD9FZf&index=13)<br>
[【完全網羅】Python dictについて](https://qiita.com/kubochiro/items/5d5cb57ee071702d15da)
    > **kataPoint:**<br>
    Dicts are better for values with labels.<br><br>
    Useful methods:<br>
    **keys()**: makes an object of keys<br>
    **values()**: makes an object of values<br>
    **items()**: makes an object of key/value pairs<br>
    **get(key, return default val when not found)**: gets value or default if not found<br>
    **pop(key, default)**: gets value and deletes from dict or return the default<br>
    **update()**: updates/adds item to dict<br>
    **clear()**:<br>
    **copy()**:<br>
    **setdefault(key, default)**: gets value or makes a new item with default value if not found<br>
    **len()**:<br>
    **dict.fromkeys(keys, value)**: sets a value for all keys in a list<br>
    **dict.popitem()**: pops random item<br>
    **dict.setdefault(key, default)**: exactly the same as setdefault but is method call on class (they are the same)
6. Generator<br>[Generators](https://www.youtube.com/watch?v=GWZf_B129zs)<br>
[Pythonのイテレータとジェネレータ](https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09)
    > **kataPoint:**<br>
    Uses the yield to return while keeping a savepoint for the next iteration. next() is called upon to get the next yield value. By using a for loop you do not need to call on next(). A generator is greatly treasured for performance boosts as it does not store all values and returns one at a time. By understanding generators, and combining them with comprehensions, you will be undefeatable ;\)
7. Comprehension<br>[List Comprehensions](youtube.com/watch?v=DUnY6l482Lk&list=PL8HmoRTjTSlEgS2GsFaDr9zDLC1xD9FZf&index=10&pp=iAQB)<br>
[List Comprehensions](https://realpython.com/list-comprehension-python/)
    > **kataPoint:**<br>
    Comprehensions not only make code more readable by having only one line, they also are better in performance. However, they can become less readable if you have multiple conditions. In this case, you might consider using a normal for loop unless performance is the higher priority. Read the second link. I highly recommend the information.