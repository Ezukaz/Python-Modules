*This project has been created as part of the 42 curriculum by `<katakaha>`.*

# Python Module 01

## Description

#### An introduction to OOP (object oriented programming)
You will learn about classes and how to use them to create wonderful scalable code that makes management easier.<br>Easy management = wonderful day.<br>Happy coding!

## Learn from Each Module

1. **ex0 - How to make an instance from a class**
2. **ex1 - How a class is used to make different instances**
3. **ex2 - How classes are used to change attributes**
4. **ex3 - Making multiple instances**
5. **ex4 - Encapsuling attributes of instances & how to access them**
6. **ex5 - Adding attributes to an instance**
7. **ex6 - How to combine all steps**

**Structure for ex6**
```
GardenManager                       ← main class
│
├── GardenStats                     ← nested class inside GardenManager
│   └── calculate stats methods
│
├── __init__                        ← stores multiple gardens
├── instance methods                ← work on a specific GardenManager instance
├── @classmethod create_garden_network()← works on the class itself
└── @staticmethod                   ← utility, needs no instance or class


Plant                               ← base class
└── FloweringPlant(Plant)           ← middle child
    └── PrizeFlower(FloweringPlant) ← grandchild
```

## Resources

1. About classes, instances, methods, self, and \_\_init__<br>[Pythonのselfとかinitを理解する](https://qiita.com/ishigen/items/2d8b6e6398743f2c8110)<br>[PythonのClassについて復習](https://qiita.com/oriefield/items/29e68ba889778e2058bf)
    > **kataPoint:**<br>
    Classes have instances and methods. All the methods take the instance as the first parameter. An instance is made with the __init__method. These methods can only be used by the instance via `instance.function`. You can use a different classes function on an instance by `Class.function(instance)`.

2. `if \_\_name__ == "\_\_main__"`<br>[Pythonのif __name__ == “__main__”:の使い方とその重要性](https://qiita.com/boku_research/items/a4f511e5912dd7153518)
   > **kataPoint:**<br>
    Use this as a safeguard against unwanted execution at import time. If you don't have this, when you import this file it will execute the main as well. With this on, main will only get executed when you execute the script file.

3. Import<br>[0からわかる import とモジュール徹底解説](https://www.kikagaku.co.jp/personal/blog/python-import)
    > **kataPoint:**<br>
    Import is used to import something into your file. Mostly used when you want to use a library with modules. You can import your own modules, too.

4. Encapsulation<br>[カプセル化と情報隠蔽](https://note.com/parklabs/n/n6a5e4181e427)<br>[ゲッター・セッターの利用](https://tech.pjin.jp/blog/2021/07/27/python_13_7/)
    > **kataPoint:**<br>
    Encapsulation, to place a variable in a protective capsule that restricts access. I would think this means using const, protected, or private. Python does not have these strict encapsulation techniques. `_` before a name is naming a name with a flag to yourself as a reminder that this shouldn't be changed lightly. `__` will convert the name to a special format, `_Class__name`. In order to change the variable, you must put in this full-name. This forces you to be very deliberate with what you do. Rule of thumb: use `_` when a child needs access to the value, and `__` when you want it locked in that class

5. Inheritance<br>[クラスの継承](https://qiita.com/nyunyu122/items/9d7395f3d4de4190a991)<br>[super()についてハッキリさせる](https://qiita.com/max_marketter/items/f88150e40fe429f3dafd)<br>[ポリモーフィズムはいいぞ](https://qiita.com/Akatsuki_py/items/3e35ba326ff254a6790d)<br>[class名を取得する(インスタンスを作らずに)](https://qiita.com/meganeo/items/f183982a169059fb4949)
    > **kataPoint:**<br>
    You can base one class on another class. This is called inheritance. The one based upon is the parent while the other is the child. `super()` is used for `__init__` when you want to initialize the parent class's attributes into the child instance. One `__init__` after another will erase the previous `__init__`. In order to prevent this you use `super()`. Nothing else is needed for you to use the parent class's other attributes. You pass like this: `class Class(Parent):`.<br>A getter&setter is needed for getting/setting a different class's encapsulated variable.

6. Staticmethod<br>[Pythonのstaticmethod()とは？意味をわかりやすく簡単に解説](https://trends.codecamp.jp/blogs/media/terminology595)
    > **kataPoint:**<br>
    `@staticmethod` is a decorator used to make a method that belongs to the class but doesn't need an instance to be called. Normally, all methods use the instance in a class, therefore, you must always have the instance `self`, as the first parameter. `staticmethod` allows you to make methods that does not need this instance.
