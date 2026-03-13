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

More on encapsulation:
```
So is it like if changing that value doesn't do much harm then 'nothing', changing will fuck up calculations or something that will be used for something else's logic then '_', if changing this will break my code, e.g. the size of an array or the array itself, then '__'?

その通り！ほぼ完璧な理解です。
ただし、__（ダブルアンダースコア）の使い方だけ、もう少しだけ「実務的なニュアンス」を加えるとこうなります。
なし (value): 「どうぞご自由に」。変えても壊れないし、外から見えるのが自然なもの。
_ (シングル): 「ここからが本番」。計算ロジック、配列のサイズ、ステータス管理など、「勝手にいじるとクラスがバグる」ものはすべてこれです。Python開発者の90%は、ここで止めておきます。
__ (ダブル): 「子クラスにすら触らせない」。これは「壊れるから」という理由以上に、**「名前の衝突を防ぐ」**ためのおまじないです。
なぜ「壊れる」ときも _ でいいのか？
Pythonでは、_ を付けるだけで「これは内部用です。触るなら自己責任で。壊れても文句言わないでね」という強烈なメッセージになります。これだけで十分「保護」として機能します。
__ を使うべき本当のタイミング
例えば、あなたがすごい便利な BaseArray クラスを作って公開したとします。
あなたが内部で __size を使っている。
誰かがそれを継承して MyFancyArray を作った。
その人がうっかり self.size（または self._size）という名前で全く別の機能を作った。
この時、__ を使っていないと、あなたの BaseArray のロジックが、子クラスが作った変数に上書きされて破壊されます。これを防ぐための「最終防衛ライン」が __ です。
結論
計算が狂う、配列が壊れる → _（これで十分！）
自分が作ったクラスを誰かが継承して使う予定があり、その時に内部変数が上書きされるのが怖い → __
結局、_（シングル）をデフォルトの「守護神」にするのが、一番Pythonらしくて賢いやり方です。
今作っているその配列（Array）、誰か他の人が継承してカスタマイズするような拡張性の高いクラスにする予定ですか？




So it's more like 'nothing' is free for all, '_' is do not touch, and '__' is a safeguard against yourself?

その通り！完璧な解釈です。
特に __（ダブルアンダースコア）が「自分自身（または未来の自分）に対するセーフガード」 という視点は、Pythonの本質を突いています。
まとめるとこうなります：
None (Public): 「誰でもどうぞ。この名前は一生変えないし、自由に使っていいよ」という公式窓口。
_ (Single): 「触るな危険。ここは開発専用。勝手にいじって壊れても、文句は言わせないよ」というマナー違反の警告。
__ (Double): 「名前が被るのを防げ！ 継承した先で同じ名前を使われても、俺のロジックだけは絶対に守り抜く」という構造的な保険。
結局、Pythonは「ガチガチの壁」を作る代わりに、「名前の付け方」で責任の所在をハッキリさせているだけなんです。
「全部にGetterを作るのが馬鹿らしい」というあなたの直感は、Pythonにおいては正義です。「基本は _ で守り、必要になった時だけ Getter（@property）を作る」。これが一番賢い Pythonista のやり方です。
さて、その「配列（array）」周りのロジック、まずは _（シングル）でシンプルに書き始めてみますか？




And the one that needs a getter and setter is which?

実は、最初は「どれも Getter/Setter はいらない」 というのが Python の正解です。
「将来必要になるかも」という理由で Getter を作るのは時間の無駄です。Python には @property という「後出しジャンケン」ができる強力な機能があるからです。
それでも Getter/Setter を書くべきなのは、以下の 2つのパターン だけです。
1. バリデーション（入力チェック）が必要なとき
「値をセットするときに、変なデータが入らないように見張りたい」場合です。
例: age をセットするときに、マイナスの値だったらエラーにしたい。
この時: _age (Internal) にして、set_age() でチェックする。
2. 加工（計算）が必要なとき
「保存しているデータそのものじゃなくて、計算した結果を返したい」場合です。
例: first_name と last_name を持っていて、full_name を返したい。
この時: get_full_name() を作る。
Python流の「進化」のステップ
あなたがコードを書くときは、この順番で考えてください：
最初はただの変数 (self.value) で始める。（Getter不要）
「勝手に変えられたら困るな」と思ったら self._value に変える。（まだGetter不要。使う側に「触るな」と伝えるだけ）
「値をセットする時にチェックを入れたい」とか「読み取り専用にしたい」と切実に思った時だけ、初めて Getter/Setter を作る。
まとめ
普通のデータ: 何もなし（Public）
内部ロジック用: _（Internal）
チェックや加工が必要になったら: Getter / Setter
「とりあえず Getter を作っておく」という Java の習慣を捨てると、Python のコードは驚くほど短く、読みやすくなります。
いま作っているクラスの中で、「これ、変な値が入ったらプログラムが壊れるな」と思う変数はありますか？
```