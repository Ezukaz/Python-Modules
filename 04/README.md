*This project has been created as part of the 42 curriculum by katakaha.*

# Python Module 04

## Description

Learn file handling in this module by playing with them. We explore opening/closing files, writing files, different types of streams, and

## Assignments

1. **ex0 - Introduction with open()**
2. **ex1 - Altering files with write()**
3. **ex2 - I/O mastering streams**
4. **ex3 - Security by 'with'**
5. **ex4 - Handling errors**

## Instructions

1. **ex0**: Create 3 txt files. 2 with various text (preferably with nl) and 1 (or more) with no text or just whitespace.
Or better yet, do ex1 first to make the files needed and transfer them to ex0.
2. **ex1**: Same as above but making file vs reading them. I made a makefile to do some cleanup after making txt files. Check it out.
3. **ex2**: Run `python3 ft_stream_management.py > output.txt 2> errors.log` to check if error msgs. `cat errors.log` to see the contents.
## Resources

1. Open<br>[open関数とは？ファイルパスや引数設定(モード)について解説](https://python-hack.net/what-is-open-function/)<br>[Python Context Manager: Syntax, Usage, and Examples](https://mimo.org/glossary/python/context-manager)
    > **kataPoint:**<br>
    Use `with` command to always close files after open was called on. `read()` will consume whole open object so if you try to call on the object again, it will be empty and useless. Use `readlines()` to get lines from object. `open()` already processes in lines. `open()` has various modes. Look them up. Default is 'r'. **CAUTION**: be careful when you `close()`. I put `close()` in 'finally' but it tried to close a file that was never opened. This will cause a crash. It happened when I tried to open a file that didn't exist. So for `r`, it doesn't exactly mean you need to cleanup whether success or not because fail could mean that it never opened. 'w' on the other hand, will most likely always open, and therefore need a cleanup for every situation, and 'finally' starts to make sense. Just use 'with' and all your problems are solved lol.
    Context managers are...I can't explain it very well but they use `__enter__` & `__exit__`. `with` is a context manager. It does a `close()` cleanup for `open()`. `with` is the equivalent of using the `finally` in a `try/except` statement.
    Use `else` to do something after a successful `try`. A celebration, so to speak.
2. Write<br>[]()
    > **kataPoint:**<br>

3. Stream<br>[]()
    > **kataPoint:**<br>
    Stdout is generally not needed as `print()` by default is stdout. Stdin, also, does not really shine as you generally want a prompt, and `input()` would be your choice. Stdin shines in shell or when you don't want a prompt. Stderr should be used at all times. <br>**Vanila usage:** `sys.stderr.write("text")` needs manual nl if you want a line<br>**More common:** print("text", file=sys.stderr) since it is `print()` you can modify the end character as you please or nl by default. **Caution**: Text is printed at the end as it goes to the stderr stream which is processed after stdout.<br>For historical conventions, the prompts of `input()` are stored in stderr. This is because they wanted to separate output data and conversational messages by the streams. All conversational messages, whether they be error related or not, are stored in stderr. This is why the prompt disappears from the terminal and appears in the stderr log when you output stderr.

4. <br>[]()
    > **kataPoint:**<br>

5. <br>[]()
    > **kataPoint:**<br>

## AMA

*"What makes a good Data Archivist? One who understands that every file is a piece of history worth preserving, and every operation is a responsibility to future generations."*
> One who has a backup plan. Get it?
1. *"What happens to the storage system if connections aren’t properly closed? Why is the disconnect protocol critical?"*
> Those connections stay open unless you close them. If you forget to close them after you use them, you might not ever be able to close them. This is called a leak. Too many of them and your computer will crash.
2. *"What’s the critical difference between extraction mode (’r’) and preservation mode (’w’)? Why is this distinction vital for archivists?"*
> `r` mode is read-only. This restricts the user to reading permissions only. They cannot alter the file but access is allowed. `w` mode allows the user permission to change the file. `w` should be used with caution as it can overwrite a file that already exists. Even if it was accidental, you might lose valuable information.
3. *"Why do the Archives maintain separate channels for standard data and alerts? What could happen if these streams were mixed?"*
> We would have a time telling them apart. Debugging becomes 100x more annoying if you have to look through standard data to find error msgs. Alerts should be handled separately is the logical move.
4. *"How does the with protocol prevent data corruption? What is the RAII principle and why is it crucial for vault security?"*
> With guarantees cleanup by using context managers. Context managers are pythons take on the RAII(Resource Acquisition Is Initialization) principal. The RAII principal is C++'s basic rule. You obtain resources at initialization of an object and releasing at destruction of object. It uses constructors to gain resources and destructors to free them. This way it automatically frees resources when leaving the scope.
5. *"What are the most dangerous threats to digital archives? How does proper crisis response prevent data loss and maintain system stability?"*
> Human error or malicious intent to destroy or steal data. We catch and handle this with try/except blocks. FileNotFoundError (missing archives), PermissionError (security breaches), and other exceptions are a few of the common errors to be found. The with statement ensures files auto-close even during crisis. We predict possible threats like ransomware or disk failure and have specific responses ready. Even if you can't 100% prevent damage, you greatly reduce the attack space and maintain system stability instead of having no backup plan.