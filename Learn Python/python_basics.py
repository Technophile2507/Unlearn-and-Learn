# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 03:46:45 2020

@author: AVI & ATHI
"""

"""
 1) Variables
****************
Everything in python is an object. Variable is a word representation of that 
object.

Rules
********
a) You can't start a variable with a number but you can have a number in 
   variable.
   eg: programming1
b) You can have underscores
   eg: programming_1
c) You can't have a number as a variable.

Define variable
*****************
To define a variable you can use an assignment operator(=).
eg:
"""
programming_languages = "Python", "Java", "C++"

"""
[anybody can look at this example and say okay I get it, it's a list 
 of prgramming languages.But unfortunately it's not a list if you are curious
 just do this]
"""

print(type(programming_languages))
"""
You can see this is a tuple

Now we are gonna try a loop

For loop
**************
A for loop will help to iterate over a number of items that a stored in a data
structure.
"""

# This is loop will print all the items in the tuple programming_languages

for language in programming_languages:
    print(language)