# Session 2 - Object Mutability and Interning

### [Class Notebook](https://github.com/abdksyed/EPAi2/blob/main/Session02_ObjectMutability_Interning/notebooks/Session%202%20-%20Object%20Mutability%20and%20Intering.ipynb)
Click on **Open in Colab** for hands-on.

### Topic Covered:
* #### Multi-Line Statements and Strings
* #### Variables and Memory References
* #### Reference Counting
* #### Garbage Collection
* #### Dynamic vs Static Typing
* #### Variable Re-Assignment
* #### Object Mutability
* #### Function Arguments & Mutability
* #### Shared References & Mutability
* #### Variable Equality
* #### Everything is an Object
* #### Python Optimizations: Interning
* #### Python Optimizations: String Interning
* #### Python Optimizations: Peephole

# Assignment 2

## Assignment Objective - Performance Testing and Memory Leakage.
The 

## Classes and Functions Used:

### Something -> Class inherited from **object**
```python
    class Something(object):
	    '''A dummy Class which is used to create Cyclic References'''
	    
	    def __init__(self):
		    super().__init__()
		    self.something_new = None    
		    
	    def __repr__(self):
	    return f'Hey You Found Something'
```
The class has only one variable 'something_new', which is used later by directly calling using the instance of the class.

### SomethingNew -> Class inherited from **object**
```python
    class  SomethingNew(object):
		'''Anothe Dummy Class which is used to create Cyclic Reference.
			Arguments:
			i -> int -> default= 0. Just a variable.
			Something -> Class Object -> default= None'''
		
		def  __init__(self, i: int = 0, something: Something = None):
			super().__init__()
			self.i = i
			self.something = something
		
		def  __repr__(self):
			return  f'Hey You Again Found Something New'
```
The class have two inputs, *i* which is an integer and another something*, which is use to assign another class object to this variable.

### add_something -> Function
```python
    def  add_something(collection: List[Something], i: int):
		'''A Function which takes a list and int as input.
		Creates Cyclic References using Two Class Objects and append
		it to the main list.'''
		
		something = Something()
		something.something_new = SomethingNew(i, something)
		collection.append(something)
```
This function creates instances of two classes *Something* and *SomethingNew*, the object of *Something* is assigned to variable *something* and the internal variable of *something* is assigned the object of *SomethingNew*
Hence creating a Cyclic Reference SUCCESSFULLY! :) :) :)

### reserved_function -> Function
```python
     def  reserved_function():
		'''To be used in future if required'''
		pass
```
This function is a stand-by function, which is kept reserved for very vital feature implementation in the coming future. :p

### clear_memory -> Function
```python
    def  clear_memory(collection: List[Something]):

		'''A function which take a list as input and performs clearing
		the list and clearing all cyclic references using garbage collector.'''
		
		collection.clear() #Empties the Entire List
		gc.collect() #Run Garbage Collector and removes all Cyclic References
```
This is the heart of the program, which prevents the program from parking and leaking the memory. It explicitly calls the Garbage Collector after clearing the list which has all(131,072) the cyclic objects appended to it.

### critical_function -> Function
```python
    def  critical_function():
		'''This Function will runs the above *add_something* fucntion for 1024*128(131,072) times 
		and create tons of cyclic references loading the memory.
		At last calling clear_memory to clean up the memory.'''
	
		collection = list()
		for i in  range(1, 1024 * 128):
			add_something(collection, i)
		clear_memory(collection)
```
This function runs the add_something function for 131,072 times and create cyclic references while also appending it to a list. And, at the end the clear_memory function is called to clear out the memory and remove all cyclic references along with clearing the list.

### compare_strings_old -> Function
```python
	   def  compare_strings_old(n):
	    '''The function has two very long strings with whitesapces, so it is not interned.
		The function take a number *n* and checks whether the two strings are exact same
		or not for n times. (Here exactly same refers to same value and in same location).
		And also, the second part in the code check for the letter 'd' in the list of 
		characters of the string for n times.'''
		
	    a = 'a long string that is not intered' * 200
	    b = 'a long string that is not intered' * 200
	    for i in  range(n):
		    if a == b:
			    pass
	    char_list = list(a)
	    for i in  range(n):
		    if  'd'  in char_list:
			    pass
```
### compare_strings_new -> Function
```python
    def compare_strings_new(n):
    '''The function has two very long strings with whitesapces, so it is not interned.
        But the string is explicitly interned using sys.inten.
        The function take a number *n* and checks whether the two strings are exact same
        or not for n times. (Here exactly same refers to same value and in same location).
        And also, the second part in the code check for the letter 'd' in the list of 
        characters of the string for n times.'''

    a = sys.intern('a long string that is not intered') * 200
    b = sys.intern('a long string that is not intered') * 200
    for _ in range(n):
        if a is b:
            pass
    char_set = frozenset(a)
    for char in char_set:
        if 'd' is char:
            pass
```
## Attributes 

### time.sleep -> Attribute in module time
```python
    time.sleep(seconds)
```
It is used to stop the python execution for the given number of seconds

### char_list -> Variable
```python
    char_list = list(a)
    char_list = set(a)
```
char_list from *list(a)* creates a list of all characters in the string.
char_list from *set(a)* creates a set of all characters in the string which are unique.

### collection -> List
```python
    collection = list()
```
The variable *collection* is a list, which is used in this program to store all the objects of the class *Something*.