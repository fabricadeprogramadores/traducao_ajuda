import os
import sqlite3
import datetime
directory = 'C:\PyHelp'

if not os.path.exists(directory):
    os.makedirs(directory)

rand_facts = '''• Exception is used as a base class for all exceptions. It's strongly recommended (but not yet required) that user exceptions are derived from this class too.
• SystemExit(Exception) is raised by the sys.exit function. If it propagates to the top level without being caught by a try-except clause, the interpreter is terminated without a traceback message.
• StandardError(Exception) is used as a base class for all standard exceptions (except SystemExit, that is).
• KeyboardInterrupt(StandardError) is raised when the user presses Control-C (or any other interrupt key). Note that this may cause strange errors if you use "catch all" try-except statements.
• ImportError(StandardError) is raised when Python fails to import a module.
• EnvironmentError is used as a base class for exceptions that can be caused by the interpreter's environment (that is, they're usually not caused by bugs in the program).
• IOError(EnvironmentError) is used to flag I/O-related errors.
• OSError(EnvironmentError) is used to flag errors by the os module.
• WindowsError(OSError) is used to flag Windows-specific errors from the os module.
• NameError(StandardError) is raised when Python fails to find a global or local name.
• UnboundLocalError(NameError) is raised if your program attempts to access a local variable before it has been assigned a value. This exception is only used in 2.0 and later; earlier versions raise a plain NameError exception instead.
• AttributeError(StandardError) is raised when Python fails to find (or assign to) an instance attribute, a method, a module function, or any other qualified name.
• SyntaxError(StandardError) is raised when the compiler stumbles upon a syntax error.
•  IndentationError(SyntaxError) is raised for syntax errors caused by bad indentation. This exception is only used in 2.0 and later; earlier versions raise a plain SyntaxError exception instead.
• TabError(IndentationError) is raised by the interpreter when the -tt option is used to check for inconsistent indentation. This exception is only used in 2.0 and later; earlier versions raise a plain SyntaxError exception instead.
• TypeError(StandardError) is raised when an operation cannot be applied to an object of the given type.
• AssertionError(StandardError) is raised when an assert statement fails (if the expression is false, that is).
• LookupError(StandardError) is used as a base class for exceptions raised when a sequence or dictionary type doesn't contain a given index or key.
• IndexError(LookupError) is raised by sequence objects when the given index doesn't exist.
• KeyError(LookupError) is raised by dictionary objects when the given key doesn't exist.
• ArithmeticError(StandardError) is used as a base class for math-related exceptions.
• OverflowError(ArithmeticError) is raised when an operations overflows (for example, when an integer is too large to fit in the given type).
• ZeroDivisionError(ArithmeticError) is raised when you try to divide a number by zero.
• FloatingPointError(ArithmeticError) is raised when a floating point operation fails.
• ValueError(StandardError) is raised if an argument has the right type, but an invalid value.
• UnicodeError(ValueError) is raised for type problems related to the Unicode string type. This is only used in 2.0 and later.
• RuntimeError(StandardError) is used for various run-time problems, including attempts to get outside the box when running in restricted mode, unexpected hardware problems, etc.
• NotImplementedError(RuntimeError) can be used to flag functions that hasn't been implemented yet, or methods that should be overridden.
• SystemError(StandardError) is raised if the interpreter messes up, and knows about it. The exception value contains a more detailed description (usually something cryptic, like
"eval_code2: NULL globals" or so). I cannot recall ever seeing this exception in over five years of full-time Python programming, but maybe that's just me.
• MemoryError(StandardError) is raised when the interpreter runs out of memory. Note that this only happens when the underlying memory allocation routines complain; you can often send your poor computer into a mindless swapping frenzy before that happens.
• NoneType The type of None.
• TypeType The type of type objects (such as returned by type()). 
• IntType The type of integers (e.g. 1).
• LongType The type of long integers (e.g. 1L).
• FloatType The type of floating point numbers (e.g. 1.0).
• ComplexType The type of complex numbers (e.g. 1.0j).
• StringType The type of character strings (e.g. ’Spam’). 
• UnicodeType The type of Unicode character strings (e.g. u’Spam’). 
• TupleType The type of tuples (e.g. (1, 2, 3, ’Spam’)). 
• ListType The type of lists (e.g. [0, 1, 2, 3]). 
• DictType The type of dictionaries (e.g. {’Bacon’: 1, ’Ham’: 0}). 
• DictionaryType An alternate name for DictType. 
• FunctionType The type of user-defined functions and lambdas. 
• LambdaType An alternate name for FunctionType. 
• CodeType The type for code objects such as returned by compile(). 
• ClassType type of user-defined classes. 
• InstanceType The type of instances of user-defined classes. 
• MethodType The type of methods of user-defined class instances. 
• UnboundMethod Type An alternate name for MethodType. 
• BuiltinFunction Type The type of built-in functions like len() or sys.exit(). 
• BuiltinMethod TypeAn alternate name for BuiltinFunction. 
• ModuleType The type of modules. 
• FileType The type of open file objects such as sys.stdout. 
• XRangeType The type of range objects returned by xrange(). 
• SliceType The type of objects returned by slice().
• EllipsisType The type of Ellipsis. 
• TracebackType The type of traceback objects such as found in sys.exc traceback. 
• FrameType The type of frame objects such as found in tb.tb frame if tb is a traceback object. 
• BufferType The type of buffer objects created by the buffer() function.
• string.capitalize()Return a copy of the string with only its first character capitalized. 
• string.center(width) Return centered in a string of length width. Padding is done using spaces. 
• string.count(sub[, start[, end ]]) Return the number of occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation. 
• string.encode([encoding[,errors]]) Return an encoded version of the string. Default encoding is the current default string encoding. errors may be given to set a different error handling scheme. The default for errors is ’strict’, meaning that encoding errors raise a ValueError. Other possible values are ’ignore’ and ’replace’.  . 
• string.endswith(suffix[, start[, end ]]) Return true if the string ends with the specified suffix, otherwise return false. With optional start, test beginning at that position. With optional end, stop comparing at that position. 
• string.expandtabs([tabsize ]) Return a copy of the string where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed. 
• string.find(sub[, start[, end ]]) Return the lowest index in the string where substring sub is found, such that sub is contained in the range [start, end). Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found. 
• string.index(sub[, start[, end ]]) Like find(), but raise ValueError when the substring is not found. 
• string.isalnum() Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise. 
• string.isalpha() Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. 
• string.isdigit()Return true if there are only digit characters, false otherwise.
• string.islower() Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise. 
• string.isspace() Return true if there are only whitespace characters in the string and the string is not empty, false otherwise.
• string.istitle() Return true if the string is a titlecased string, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise. 
• string.isupper() Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise. 
• string.join(seq) Return a string which is the concatenation of the strings in the sequence seq. The separator between elements is the string providing this method. 
• string.ljust(width) Return the string left justified in a string of length width. Padding is done using spaces. The original string is returned if width is less than len(s). 
• string.lower() Return a copy of the string converted to lowercase. 
• string.lstrip() Return a copy of the string with leading whitespace removed.
• string.replace(old, new[, maxsplit]) Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument maxsplit is given, only the first maxsplit occurrences are replaced. 
• string.rfind(sub [,start [,end ]]) Return the highest index in the string where substring sub is found, such that sub is contained within s[start,end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
• string.rindex(sub[, start[, end ]]) Like rfind() but raises ValueError when the substring sub is not found. 
• string.rjust(width) Return the string right justified in a string of length width. Padding is done using spaces. The original string is returned if width is less than len(s). • string.rstrip() Return a copy of the string with trailing whitespace removed. 
• string.split([sep [,maxsplit]]) Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done. If sep is not specified or None, any whitespace string is a separator. 
• string.splitlines([keepends]) Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
• string.startswith(prefix[, start[, end ]]) Return true if string starts with the prefix, otherwise return false. With optional start, test string beginning at that position. With optional end, stop comparing string at that position. 
• string.strip() Return a copy of the string with leading and trailing whitespace removed.
• string.swapcase() Return a copy of the string with uppercase characters converted to lowercase and vice versa. 
• string.title() Return a titlecased version of, i.e. words start with uppercase characters, all remaining cased characters are lowercase. 
• string.translate(table[, deletechars]) Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256. 
• string.upper() Return a copy of the string converted to uppercase.
• file.close() Close the file. A closed file cannot be read or written anymore. Any operation which requires that the file be open will raise a ValueError after the file has been closed. Calling close() more than once is allowed. 
• file.flush() Flush the internal buffer, like stdio’s fflush(). This may be a no-op on some file-like objects. 
• file.isatty() Return true if the file is connected to a tty(-like) device, else false. Note: If a file-like object is not associated with a real file, this method should not be implemented. 
• file.fileno() Return the integer “file descriptor” that is used by the underlying implementation to request I/O operations from the operating system. This can be useful for other, lower level interfaces that use file descriptors, e.g. module fcntl or os.read() and friends. Note: File-like objects which do not have a real file descriptor should not provide this method! 
• file.read([size ]) Read at most size bytes from the file (less if the read hits EOF before obtaining size bytes). If the size argument is negative or omitted, read all data until EOF is reached. The bytes are returned as a string object. An empty string is returned when EOF is encountered immediately. (For certain files, like ttys, it makes sense to continue reading after an EOF is hit.) Note that this method may call the underlying C function fread() more than once in an effort to acquire as close to size bytes as possible. 
• file.readline([size ]) Read one entire line from the file. A trailing newline character is kept in the string7 (but may be absent when  ends with an incomplete line). If the size argument is present and non-negative, it is a maximum byte count and an incomplete line may be returned. An empty string is returned when EOF is hit immediately. Note: Unlike stdio’s fgets(), the returned string contains null characters (’\0’) if they occurred in the input. 
• file.readlines([sizehint]) Read until EOF using readline() and return a list containing the lines thus read. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read. Objects implementing a file-like interface may choose to ignore sizehint if it cannot be implemented, or cannot be implemented efficiently. 
• file.xreadlines() Equivalent to xreadlines.xreadlines(file). (See the xreadlines module for more information.)  . 
• file.seek(offset[, whence ]) Set the file’s current position, like stdio’s fseek(). The whence argument is optional and defaults to 0 (absolute file positioning); other values are 1 (seek relative to the current position) and 2 (seek relative to the file’s end). There is no return value. Note that if the file is opened for appending (mode ’a’ or ’a+’), any seek() operations will be undone at the next write. If the file is only opened for writing in append mode (mode ’a’), this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode ’a+’). 
• file.tell() Return the file’s current position, like stdio’s ftell(). 
• file.truncate([size ]) Truncate the file’s size. If the optional size argument present, the file is truncated to (at most) that size. The size defaults to the current position. Availability of this function depends on the operating system version (for example, not all UNIX versions support this operation). 
• file.write(str) Write a string to the file. There is no return value. Note: Due to buffering, the string may not actually show up in the file until the flush() or close() method is called. 
• file.writelines(list) Write a list of strings to the file. There is no return value. (The name is intended to match readlines(); writelines() does not add line separators.) File objects also offer a number of other interesting attributes. These are not required for file-like objects, but should be implemented if they make sense for the particular object. 
• file.closed Boolean indicating the current state of the file object. This is a read-only attribute; the close() method changes the value. It may not be available on all file-like objects. 
• file.mode The I/O mode for the file. If the file was created using the open() built-in function, this will be the value of the mode parameter. This is a read-only attribute and may not be present on all file-like objects. 
• file.name If the file object was created using open(), the name of the file. Otherwise, some string that indicates the source of the file object, of the form ‘<...>’. This is a read-only attribute and may not be present on all file-like objects.
• abs(x) Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned. 
• apply(function, args[, keywords]) The function argument must be a callable object (a user-defined or built-in function or method, or a class object) and the args argument must be a sequence (if it is not a tuple, the sequence is first converted to a tuple). The function is called with args as the argument list; the number of arguments is the the length of the tuple. (This is different from just calling func(args), since in that case there is always exactly one argument.) If the optional keywords argument is present, it must be a dictionary whose keys are strings. It specifies keyword arguments to be added to the end of the the argument list. 
• buffer(object[, offset[, size ]]) The object argument must be an object that supports the buffer call interface (such as strings, arrays, and buffers). A new buffer object will be created which references the object argument. The buffer object will be a slice from the beginning of object (or from the specified offset). The slice will extend to the end of object (or will have a length given by the size argument). 
• callable(object) Return true if the object argument appears callable, false if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); class instances are callable if they have a call () method.
• chr(i) Return a string of one character whose ASCII code is the integer i, e.g., chr(97) returns the string ’a’. This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. 
• cmp(x, y) Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y. 
• coerce(x, y) Return a tuple consisting of the two numeric arguments converted to a common type, using the same rules as used by arithmetic operations. compile(string, filename, kind) Compile the string into a code object. Code objects can be executed by an exec statement or evaluated by a call to eval(). The filename argument should give the file from which the code was read; pass e.g. ’<string>’ if it wasn’t read from a file. The kind argument specifies what kind of code must be compiled; it can be ’exec’ if string consists of a sequence of statements, ’eval’ if it consists of a single expression, or ’single’ if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something else than None will printed). 
• complex(real[, imag ]) Create a complex number with the value real + imag*j or convert a string or number to a complex number. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the function serves as a numeric conversion function like int(), long() and float(); in this case it also accepts a string argument which should be a valid complex number. 
• delattr(object, name) This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, ’foobar’) is equivalent to del x.foobar. 
• dir([object]) Without arguments, return the list of names in the current local symbol table. 
• divmod(a, b) Take two numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as (a / b, a % b). For floating point numbers the result is (q, a %bb), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b). 
• eval(expression[, globals[, locals]]) The arguments are a string and two optional dictionaries. The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local name space. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where eval is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example: 
>>> x = 1 
>>> print eval(’x+1’) 
2 This function can also be used to execute arbitrary code objects (e.g. created by compile()). In this case pass a code object instead of a string. The code object must have been compiled passing ’eval’ to the kind argument. Hints: dynamic execution of statements is supported by the exec statement. Execution of statements from a file is supported by the execfile() function. The globals() and locals() functions returns the current global and local dictionary, respectively, which may be useful to pass around for use by eval() or execfile(). 
• execfile(file[, globals[, locals]]) This function is similar to the exec statement, but parses a file instead of a string. It is different from the import statement in that it does not use the module administration — it reads the file unconditionally and does not create a new module.8 The arguments are a file name and two optional dictionaries. The file is parsed and evaluated as a sequence of Python statements (similarly to a module) using the globals and locals dictionaries as global and local names- pace. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where execfile() is called. The return value is None. 
• filter(function, list) Construct a list from those elements of list for which function returns true. If list is a string or a tuple, the result also has that type; otherwise it is always a list. If function is None, the identity function is assumed, i.e. all elements of list that are false (zero or empty) are removed. 
• float(x) Convert a string or a number to floating point. If the argument is a string, it must contain  a possibly signed dec-imal or floating point number, possibly embedded in whitespace; this behaves identical to string.atof(x). Otherwise, the argument may be a plain or long integer or a floating point number, and a floating point number with the same value (within Python’s floating point precision) is returned.
• getattr(object, name[, default]) Return the value of the named attributed of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, ’foobar’) is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised. 
• globals() Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called). 
• hasattr(object, name) The arguments are an object and a string. The result is 1 if the string is the name of one of the object’s attributes, 0 if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an exception or not.) 
• hash(object) Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, e.g. 1 and 1.0). 
• hex(x) Convert an integer number (of any size) to a hexadecimal string. The result is a valid Python expression. Note: this always yields an unsigned literal, e.g. on a 32-bit machine, hex(-1) yields ’0xffffffff’. When evaluated on a machine with the same word size, this literal is evaluated as -1; at a different word size, it may turn up as a large positive number or raise an OverflowError exception. 
• id(object) Return the ‘identity’ of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects whose lifetimes are disjunct may have the same id() value. (Implementation note: this is the address of the object.) 
• input([prompt]) Equivalent to eval(raw input(prompt)). Warning: This function is not safe from user errors! It expects a valid Python expression as input; if the input is not syntactically valid, a SyntaxError will be raised. Other exceptions may be raised if there is an error during evaluation. (On the other hand, sometimes this is exactly what you need when writing a quick script for expert use.) If the readline module was loaded, then input() will use it to provide elaborate line editing and history features. Consider using the raw input() function for general input from users.
• int(x[, radix ]) Convert a string or number to a plain integer. If the argument is a string, it must contain a possibly signed decimal number representable as a Python integer, possibly embedded in whitespace; this behaves identical to 
• string.atoi(x[, radix ]). The radix parameter gives the base for the conversion and may be any integer in the range [2, 36], or zero. If radix is zero, the proper radix is guessed based on the contents of string; the interpretation is the same as for integer literals. If radix is specified and x is not a string, TypeError is raised. Otherwise, the argument may be a plain or long integer or a floating point number. Conversion of floating point numbers to integers is defined by the C semantics; normally the conversion truncates towards zero.9 
• intern(string) Enter string in the table of “interned” strings and return the interned string – which is string itself or a copy. Interning strings is useful to gain a little performance on dictionary lookup – if the keys in a dictionary are interned, and the lookup key is interned, the key comparisons (after hashing) can be done by a pointer compare instead of a string compare. Normally, the names used in Python programs are automatically interned, and the dictionaries used to hold module, class or instance attributes have interned keys. Interned strings are immortal (i.e. never get garbage collected). 
• isinstance(object, class) Return true if the object argument is an instance of the class argument, or of a (direct or indirect) subclass thereof. Also return true if class is a type object and object is an object of that type. If object is not a class instance or a object of the given type, the function always returns false. If class is neither a class object nor a type object, a TypeError exception is raised. 
• issubclass(class1, class2) Return true if class1 is a subclass (direct or indirect) of class2. A class is considered a subclass of itself. If either argument is not a class object, a TypeError exception is raised. 
• len (s) Return the length (the number of items) of an object. The argument may be a sequence (string, tuple or list) or a mapping (dictionary). 
• list(sequence) Return a list whose items are the same and in the same order as sequence’s items. If sequence is already a list, a copy is made and returned, similar to sequence[:]. For instance, list(’abc’) returns returns [’a’, ’b’, ’c’] and list( (1, 2, 3) ) returns [1, 2, 3].
• locals() Return a dictionary representing the current local symbol table. Warning: The contents of this dictionary should not be modified; changes may not affect the values of local variables used by the interpreter. 
• long(x[, radix ]) Convert a string or number to a long integer. If the argument is a string, it must contain a possibly signed number of arbitrary size, possibly embedded in whitespace; this behaves identical to string.atol(x). The radix argument is interpreted in the same way as for int(), and may only be given when x is a string. Otherwise, the argument may be a plain or long integer or a floating point number, and a long integer with the same value is returned. Conversion of floating point numbers to integers is defined by the C semantics; see the description of int(). 
• map(function, list, ...) Apply function to every item of list and return a list of the results. If additional list arguments are passed, function must take that many arguments and is applied to the items of all lists in parallel; if a list is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple list arguments, map() returns a list consisting of tuples containing the corresponding items from all lists (i.e. a kind of transpose operation). The list arguments may be any kind of sequence; the result is always a list. 
• max(s[, args...]) With a single argument s, return the largest item of a non-empty sequence (e.g., a string, tuple or list). With more than one argument, return the largest of the arguments. 
• min(s[, args...]) With a single argument s, return the smallest item of a non-empty sequence (e.g., a string, tuple or list). With more than one argument, return the smallest of the arguments.
• oct(x) Convert an integer number (of any size) to an octal string. The result is a valid Python expression. Note: this always yields an unsigned literal, e.g. on a 32-bit machine, oct(-1) yields ’037777777777’. When evaluated on a machine with the same word size, this literal is evaluated as -1; at a different word size, it may turn up as a large positive number or raise an OverflowError exception.
• ord(c) Return the ASCII value of a string of one character or a Unicode character. E.g., ord(’a’) returns the integer 97, ord(u’ u2020’) returns 8224. This is the inverse of chr() for strings and of unichr() for Unicode characters. 
• pow(x, y[, z]) Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z). The arguments must have numeric types. With mixed operand types, the rules for binary arithmetic operators apply. The effective operand type is also the type of the result; if the result is not expressible in this type, the function raises an exception; e.g., pow(2, -1) or pow(2, 35000) is not allowed.
• range([start,] stop[, step ]) This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. The arguments must be plain integers. If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. The full form returns a list of plain integers [start, start + step, start + 2 * step, ...]. If step is positive, the last element is the largest start + i * step less than stop; if step is negative, the last element is the largest start + i * step greater than stop. step must not be zero (or else ValueError is raised). 
• reduce(function, sequence[, initializer]) Apply function of two arguments cumulatively to the items of sequence, from left to right, so as to reduce the sequence to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If the optional initializer is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty. 
• reload(module) Re-parse and re-initialize an already imported module. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (i.e. the same as the module argument).
• repr(object) Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(). 
• round(x[, n ]) Return the floating point value x rounded to n digits after the decimal point. If n is omitted, it defaults to zero. The result is a floating point number. Values are rounded to the closest multiple of 10 to the power minus n; if two multiples are equally close, rounding is done away from 0 (so e.g. round(0.5) is 1.0 and round(- 0.5) is -1.0).
• setattr(object, name, value) This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, ’foobar’, 123) is equivalent to x.foobar = 123.
• slice([start,] stop[, step ]) Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used, e.g. for ‘a[start:stop:step]’ or ‘a[start:stop, i]’. 
• str(object) Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string. 
• tuple(sequence) Return a tuple whose items are the same and in the same order as sequence’s items. If sequence is already a tuple, it is returned unchanged. For instance, tuple(’abc’) returns returns (’a’, ’b’, ’c’) and tuple([1, 2, 3]) returns (1, 2, 3). 
• type(object) Return the type of an object. The return value is a type object. The standard module types defines names for all built-in types. For instance: 
>>> import types 
>>> if type(x) == types.StringType: print "It’s a string" unichr(i) 
Return the Unicode string of one character whose Unicode code is the integer i, e.g., unichr(97) returns the string u’a’. This is the inverse of ord() for Unicode strings. The argument must be in the range [0..65535], inclusive. ValueError is raised otherwise.  .
• unicode(string[, encoding[, errors]]) Decodes string using the codec for encoding. Error handling is done according to errors. The default behavior is to decode UTF-8 in strict mode, meaning that encoding errors raise ValueError. See also the codecs module.  . 
• vars([object]) Without arguments, return a dictionary corresponding to the current local symbol table. With a module, class or class instance object as argument (or anything else that has a dict attribute), returns a dictionary corresponding to the object’s symbol table. The returned dictionary should not be modified: the effects on the corresponding symbol table are undefined.11 
• xrange([start,] stop[, step ]) This function is very similar to range(), but returns an “xrange object” instead of a list. This is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all si- multaneously. The advantage of xrange() over range() is minimal (since xrange() still has to create the values when asked for them) except when a very large range is used on a memory-starved machine (e.g. MS-DOS) or when all of the range’s elements are never used (e.g. when the loop is usually terminated with break). 
• zip(seq1, ...) This function returns a list of tuples, where each tuple contains the i-th element from each of the argument sequences. At least one sequence is required, otherwise a TypeError is raised. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple argument sequences which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. 

'''

op='C:\PyHelp\\randinfo.txt'
file_exists = os.path.isfile(op) 
 
if not file_exists:
   
    x = open(op,"w")
    x.write(rand_facts)


