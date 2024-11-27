# remove duplicates from given array
def remove_duplicates(arr):
    return list(set(arr))

arr1 = [1,1,1,1,2,2,2,33,3,4,4,4,4,5]
print(remove_duplicates(arr1))

# fibonacci series

def fibonacci(n):
    a ,b=0 ,1
    for _ in range(n):
        print(a,"")
        a, b = b, a+b
fibonacci(10)
    
# replace space with a given character 

input1 = "abc ef hi jk"
character = 'a'

output = input1.replace(' ', character)
print(output)

# Lambda function : Lambda functions are small anonymous functions defined with the lambda keyword. 
# They can have any number of arguments but only one expression.

add1 = lambda x, y : x+y
print(add1(4,5))

numbers1 = [1,2,3,4,5,6,7,8,9,10]
output_even = list(filter(lambda x: x%2 ==0, numbers1))
print(output_even)

#Set_index vs Reset_index
#set_index: Sets a DataFrame one or more column as the index.
# reset_index: Resets the index to the default integer index.
import pandas as pd

data = {'ID' : [101,102,103],
        'Name': ['adviteeya', 'nirvaan', 'sandhya'],
        'Age': [35,1,32]}
df = pd.DataFrame(data)
print(df)
df_with_index = df.set_index('ID')
print(df_with_index)
df1 = df_with_index.reset_index()
print(df1)



df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# Display default index
print(df2)
print(df2.index)

# Set a column as an index
df3 = df2.set_index('A', inplace=True)
print(df3)

'''Pandas Merge vs Join vs Concat
Merge: Combines DataFrames based on keys or indices. Horizontally.
Join: Similar to merge, but uses the index by default. ( left, right, inner, outer)
Concat: Concatenates DataFrames along a particular axis.( vertical)
'''
# pandas program to rename columns
df4 = pd.DataFrame({'name': ["akansha", "renu", "binu"], 'age': [23,45,67]})
print(df4)
df5 = df4.rename(columns={'name':'first_name'})
print(df5)

#Pandas Program to Select Rows Where the Score is Missing (NaN)
import pandas as pd
import numpy as np

df6 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'score': [np.nan, 85, np.nan]})
print(df6)
missing_score_rows = df6[df6['score'].isna()]
print(missing_score_rows)

#15. Pandas Program to Convert a NumPy Array to a Pandas Series

array = np.array([1, 2, 3, 4, 5])
print(array)
series = pd.Series(array)
print(series)

#Reverse a String/List Using Slicing
# Reverse a string
reversed_string = "example"[::-1]
print(reversed_string)

# Reverse a list
reversed_list = [1, 2, 3, 4, 5][::-1]
print(reversed_list)

'''Pickling vs Unpickling
Pickling: The process of converting a Python object into a byte stream.
Unpickling: The process of converting a byte stream back into a Python object.

Memory Management in Python
Python uses automatic memory management, including garbage collection. 
The gc module provides an interface to the garbage collector. 
Memory is managed using reference counting and cyclic garbage collection.


In Python, *args and **kwargs are special syntax used in function definitions to pass a variable number of arguments to a function. 
Here's a detailed explanation with examples:



1. What is *args?
•	Definition: *args allows a function to accept any number of positional arguments.
•	Type: The arguments passed as *args are stored as a tuple inside the function.
________________________________________
How to Use *args
Example 1: Accepting Multiple Arguments
'''
def sum1(*args):
   total = sum(args)
   return(total)

print(sum1(1,2,3,4,5,6))
print(sum1(5,6))
#When to Use *args
#	When you don't know how many positional arguments will be passed in advance.
#	For creating flexible and reusable functions.
# What is **kwargs?
#	Definition: **kwargs allows a function to accept any number of keyword arguments 
#   (arguments passed as key=value pairs).
#	Type: The arguments passed as **kwargs are stored as a dictionary inside the function.
def key_value ( **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
key_value(name="alice", age=21, city="delhi")

"""
2. Shallow vs Deep Copy
Shallow Copy: Creates a new object but inserts references into it to the objects found in the original. Changes to mutable objects in the copy will reflect in the original.
Deep Copy: Creates a new object and recursively copies all objects found in the original. Changes to mutable objects in the copy do not affect the original.
3. Decorators
Decorators are a way to modify or enhance functions or methods without changing their actual code. They are often used for logging, enforcing access control, instrumentation, and caching.

4. Generators
Generators are a type of iterable, like lists or tuples. Unlike lists, they do not store their contents in memory; instead, they generate items on the fly using the yield keyword. This makes them more memory efficient for large datasets.

5. Access Specifiers in Python
Python does not have traditional access specifiers like public, protected, and private. Instead, it uses naming conventions:

_single_leading_underscore: Weak "internal use" indicator.
__double_leading_underscore: Triggers name mangling to avoid conflicts in subclasses.
__double_leading_and_trailing_underscore__: Reserved for special use in the language.
6. Class vs Static Methods
Class Methods: Use the @classmethod decorator and take cls as the first parameter. They can modify class state that applies across all instances.
Static Methods: Use the @staticmethod decorator and do not take self or cls as the first parameter. They behave like plain functions but belong to the class's namespace.
7. Unit Tests in Python
Unit tests are used to validate that individual units of code (functions, methods) work as expected. Python's unittest module provides a framework for creating and running tests.

8. GIL (Global Interpreter Lock)
The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously. This simplifies memory management but can be a bottleneck in CPU-bound multi-threaded programs.

9. Exceptions
Exceptions are errors detected during execution. Python uses a try-except block to handle exceptions. Common exceptions include ValueError, TypeError, and IndexError.


"""