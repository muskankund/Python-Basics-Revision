'''Errors cannot be handled, while Python exceptions can be handled at the run time. An error can be a syntax (parsing) error, while there can be many types of exceptions that could occur during the execution and are not unconditionally inoperable. An Error might indicate critical problems that a reasonable application should not try to catch, while an Exception might indicate conditions that an application should try to catch. Errors are a form of an unchecked exception and are irrecoverable like an OutOfMemoryError, which a programmer should not try to handle.'''

#SYNTAX ERRORS:
'''	Syntax errors often called as parsing errors, are predominantly caused when the parser detects a syntactic issue in your code.'''
g=8
h=10
i= g h
print(i) #syntax error

#EXCEPTION:
'''	Even if the syntax of a statement or expression is correct, it may still cause an error when executed. Python exceptions are errors that are detected during execution and are not unconditionally fatal: you will soon learn in the tutorial how to handle them in Python programs. An exception object is created when a Python script raises an exception. If the script explicitly doesn't handle the exception, the program will be forced to terminate abruptly.'''
a=2
b='DATACAMP'
x=a+b  
print(x)   #example 1
c=100
d=0
e=c/d
print(e) #example 2
