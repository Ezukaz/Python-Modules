*This project has been created as part of the 42 curriculum by katakaha.*

# Python Module 05

## Description

## Assignments

1. **ex0 -
2. **ex1 -
3. **ex2 -


## Instructions

1. **ex0**:
2. **ex1**:
3. **ex2**:

## Resources

1. <br>[]()
    > **kataPoint:**<br>

2. <br>[]()
    > **kataPoint:**<br>

3. <br>[]()
    > **kataPoint:**<br>

## AMA

1. *"How does method overriding enable the same processing interface to
handle completely different data types? What makes this approach
more powerful than separate processing functions?"*
> By writing code specific for each class method's needs. By separating each child class specific code and base class code you avoid redundant code. This is good for future development if you ever need to change code.
2. *"How does polymorphism allow the StreamProcessor to handle different
stream types without knowing their specific implementations? What
are the benefits of this design approach?"*
> By sharing the same interface. Each class object knows what it is so StreamProcessor only needs to call on the interface of the object. This separates responsibilities and separate actions for each individual object. It also make code more scaleable and easier to manage as the caller only calls the same method name. If you want to change the method of an individual instance, all you just have to do is change the code for that specific class method and not every method of all related classes.
3. *"How does the combination of method overriding and subtype
polymorphism enable building scalable, maintainable data processing
systems? What real-world engineering problems does this approach
solve?"*
> As explained above
