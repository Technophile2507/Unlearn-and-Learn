# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:53:49 2020

@author: AVI & ATHI
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:16:36 2020

@author: AVI & ATHI
"""

"""
Today we are gonna make a Tic Tac Toe game using Python 3. The best way to 
learn is to find a probblem and then break em down into several pieces and then
solve it one by one.

1) Inorder to build a game we need to visualize the game map 
[ We gonna use list and list of list to build this game]
"""

game = (0, 0, 0,
       0, 0, 0,
       0, 0, 0)

# the result will be tuple flat 0's and since it's a tuple so it's immutable
print(game)

"""
 so let's change the variable game to a list
"""
# just replace paranthesis with a square bracket to change game to a list

game = [0, 0, 0,
       0, 0, 0,
       0, 0, 0]

print(type(game))

"""
Still it's all flat but that's not how we need it but now we can change the
items in a list
"""
# add square brackets for each row

game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

print(game)

""" 
Now they are seperated still they don;t appear as new lines
let's iterate over the list and see if it works
"""

# for row in game:
#     print(row )
    
"""
Now we need to take user input in specific postions.
How do we do that ?

We can do that by giving labels to each rows and columns
"""

print(" 0  1  2")
count = 0
for row in game:
    print(count,row )
    count+=1

"""
But the above method is not the best way to do it but it does get the job done.
now let's try to do it in some other way

We can use enumerate built in function
Enumerate iterate for a collection of values and it returns the index and the value
You can get count from enumerate
"""
print("   a  b  c")
for count,row in enumerate(game):
    print(count,row)
    count+=1
    
"""
To be continued ...
"""


