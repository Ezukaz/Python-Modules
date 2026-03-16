*This project has been created as part of the 42 curriculum by `<katakaha>`.*

# Python Module 02

## Description

Learn the basics of error handling by using the Exception class.

## Learn from Each Assignment

1. **ex0 - Exception with try/except**
2. **ex1 - Different Kinds of exceptions**
3. **ex2 - Custom Exceptions**
4. **ex3 - **
5. **ex4 - **
6. **ex5 - All together now**

## Resources

1. Catching Errors<br>[例外処理（try-except）を活用しよう](https://qiita.com/suipy/items/9d02e197df813f3c2fab)<br>[Pythonの例外処理（try-except）について解説します！](https://techplay.jp/column/1831)<br>[【完全解説！】Pythonの例外処理を基礎から実務レベルまで完全にマスターする](https://zenn.dev/tigrebiz/articles/python-try-exception)
    > *kataPoint:*<br>
    Try will try the code in the block. If it couldn't do it then except will handle the error by: if you give it a Class (there are 63 classes that inherit from Exception, check them out by `print(dir(__builtins__))`) you can handle each one differently. `except Class as e` will store the error as an object in `e`. You can handle different class errors the same with paranthesis (`except (ZeroDivisionError, TypeError)`). Not having a type class will handle all types the same with the code that you set under the `except`.<br>
    `else` after `except` is for an action when success. `finally` is for an action to do at the end whether or not success
2. Different Kinds of Errors<br>[What types of exceptions should you catch?](https://www.pythonmorsels.com/what-types-of-exceptions-should-you-catch/)
    > *kataPoint:*<br>
    **Exceptions serve several key purposes:
    Preventing program termination, graceful error recovery, separating error-handling code, and signaling error conditions.**<br>
    Preventing Program Termination: When an error occurs (e.g., a file not found or a division by zero), an exception is "raised". If unhandled, this terminates the program. Exception handling allows the program to catch the error and continue running.
    Graceful Error Recovery: Instead of abrupt failure, exceptions let the program respond to the problem in a controlled manner, such as asking for valid input again, logging the error for debugging, or providing a user-friendly message.
    Separating Error-Handling Code: Exceptions separate the main logic of a program from the code that deals with errors, making the primary code flow cleaner and easier to read.
    Signaling Error Conditions: Developers can also raise their own exceptions to signal that a function has received invalid input or encountered a condition it cannot handle under normal flow, effectively using the exception system for error signaling.

    Key Concepts and Syntax
    The primary keywords for handling exceptions in Python are try, except, else, and finally.
    try: This block contains the code that might cause an error.
    except: If an exception occurs within the try block, the execution flow jumps to the corresponding except block, where the error can be handled. You can specify which type of exception to catch (e.g., ValueError, FileNotFoundError).
    else: The code in this optional block is executed only if the try block runs without raising any exceptions.
    finally: The code in this optional block is always executed, regardless of whether an exception occurred or was handled. This is useful for cleanup operations, like closing files or network connections.

    Common Built-in Exceptions
    Python has a rich hierarchy of built-in exceptions derived from the base class BaseException. Common examples include:
    ZeroDivisionError: Occurs when dividing by zero.
    TypeError: Occurs when an operation is performed on an inappropriate data type.
    ValueError: Occurs when a function receives an argument of the correct type but an invalid value.
    FileNotFoundError: Occurs when a file requested (e.g., for reading) does not exist.
    IndexError: Occurs when an index is out of range for a list or other sequence.

    By using exception handling, developers can write more resilient programs that can gracefully manage unexpected situations during runtime. The Python documentation on Built-in Exceptions provides a complete list and hierarchy.
3. Custom Errors<br>[pythonの自作Exceptionで変数を含むエラー内容を出力する](https://qiita.com/s_szk/items/e6b932816667e7974f0e)<br>[Python Custom Exceptions](https://codingnomads.com/python-throw-exception-custom)
    > *kataPoint:*<br>
    In Python, you create **custom exceptions** by inheriting from the built-in Exception class to handle specific error cases that standard exceptions (like ValueError) don't cover.
    ### 1. Basic Definition
    The simplest way is to define a class using pass. It is a best practice to end the class name with "Error".
```python
class MyCustomError(Exception):
    """Base class for exceptions in this module."""
    pass

# Usage
try:
    raise MyCustomError("Something went wrong")
except MyCustomError as e:
    print(f"Caught: {e}")
```
- Reference: [Python Custom Exceptions - Programming For Beginners](https://www.youtube.com) (06:56)
    ### 2. Adding Custom Data
    Override __init__ to store extra info, such as error codes or the specific value that triggered the failure.
```python
class ValueTooSmallError(Exception):
    def __init__(self, value, message="Value is too small"):
        self.value = value
        self.message = f"{message}: {value}"
        super().__init__(self.message)

# Usage
num = 5
if num < 10:
    raise ValueTooSmallError(num)
```
- Reference: [How to create custom exceptions in Python - Techizall](https://www.youtube.com) (02:16)
    ### 3. Why Use Custom Exceptions?
    - Specificity: Use names that describe your domain (e.g., InsufficientFundsError).
    - Selective Catching: Allows you to catch your specific errors while letting others (like KeyError) propagate.
    - Readability: Makes it obvious to other developers what went wrong without checking the error message string.
    ### 4. Best Practices: Hierarchy
    For larger projects, create a base class for your app and inherit from it to organize errors.
```python
class AppError(Exception): """Base for all app errors"""
class DatabaseError(AppError): """DB specific error"""
class UserNotFoundError(AppError): """User specific error"""

# Catching AppError will catch both sub-classes
```

4. Description<br>[link title]()
    > *kataPoint:*<br>
    
5. Description<br>[link title]()
    > *kataPoint:*<br>
    
6. Description<br>[link title]()
    > *kataPoint:*<br>
    
