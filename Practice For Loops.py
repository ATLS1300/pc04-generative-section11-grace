#!/usr/bin/env python
# coding: utf-8

# # We are learning about for loops today!

# For loops are an important part of creating generative and pattern-based art. We can make polygons, spirographs and more complex patterns by using for loops. Let's get familliar!
# 
# **Remember:** press SHIFT + ENTER to execute the code in the cell (gray blocks with line numbers). <br>
# If you get an error printed below, you have a mistake that must be fixed in that cell. <br>
# If nothing is shown below the gray cell block, you've gotten it right!

# ## 1. Using `range()` to determine number of loops
# 1. For loops allow predetermined numbers of repeats, or **iterations** in programs. This means that we know how many times we want a task to repeat. Predetermined looping requires data structures in order to run. For loops will use the number of elements (or individual values) stored in the data structure to determine the number of times the loop runs. Let's start with a simple loop.
# 
# In the cell below, the function `range()` is used with the value `4` to create a loop that repeats 4 times.
# Change the value to 10 and see how many times the loop repeats.

# In[ ]:


for i in range(4):
    print('Repeat')


# The variable name `i` is used for the **index variable**. The index variable changes with each iteration (or repeat) of the loop! Let's see what the values of i are, as the loop repeats. 
# Copy the loop above, and instead of `'Repeat'` type in the **index variable** name `i` (which is short for index).

# In[2]:


for i in range(4):
    print('i')


# With the first iteration, i = 0, the second iteration, i = 1, and so forth. This makes for a handy counter AND a handy index, when trying work with multiple values in a list (or tuple!), one after another.

# ## 2. Stepping through values in data structures
# 2. For loops can work with any data structure, not just ranges. Let's see the different ways we can work with a list to step through values inside the list
# 
# In the space below, create a list called `numLoops` that has 3 values. They can be anything you like (ex types: `str`, `int`, `bool`)!

# In[16]:


numLoops = ["monday", "tuesday", "wednesday"]


# Now let's use a loop to print the values of each element. This is the simplest type of for loop.
# 
# **A note on names:**<br>
# It's good practice to use a give your **index variable** a descriptive name. The name should indicate how you are using your index variable! In the first example, we're merely using the index variable to count the number of repeats the loop makes, so we used `i`. But in this example, we use the value in the element in the loop itself, so we use `elem`.

# In[17]:


for elem in numLoops:
    print(elem)


# The index variable, `elem` stores each value in numLoops, which updates with each iteration. 
# 
# Try changing the first element of numLoops to `0` using indexing:

# In[18]:


numLoops[0] = 0
# add your value to the righthand side


# Now change the number of elements in the list 'numLoops'. For this, we can use a hidden function that comes with all lists. We can access these "hidden" functions by using dot notation.
# 
# Add a value in the parentheses below to append (or attach) an extra element onto the end of our list.
# 

# In[19]:


numLoops.append("weekdays")


# Now let's run the loop again. What has changed?

# In[20]:


for elem in numLoops:
    print(elem)


# # Check your answers
# Run the cell below to check your answers so far!

# In[21]:


assert type(numLoops) == type([]), "Whoops, your numLoops variable isn't a list! Redo the task in Section 2" # check that numLoops is a list
assert len(numLoops) == 4, "You do not have the right number of elements in your numLoops variable. Please check your definition!"# numLoops starts off with 3 values, and 2 more should be added
assert numLoops[0] == 0, "numLoops[0] does not have a value of 0. Did you run that cell? (SHIFT + ENTER)"# change the first value using indexing

print('Nice work, keep going!')


# ## 3. Incrementally changing values in for loops
# Oftentimes, we'll want to change a value as we progress through a loop. This is useful for animations, or creating color gradients (see the **thought project** below!)
# 
# For this, we can use the **assignment operators** `+=` or `-=`
# The syntax to use theses is:<br>
#     `variable += increment`<br>
#     where `variable` and `increment` are numeric variables (like `int` or `float`). 
# 
# When this line is executed, the variable value will change by the increment on the right.<br>
# For example, 
# if `startVal = 0`, then <br>
# `startVal -= 10` subtracts 10 from the value of `startVal`(now startVal has a value of -10)
# 
# 
# This is the same as writing:<br>
# `startVal = startVal - 10`<br>
# 
# Now it's your turn. Try adding to a value in a for loop. We'll add the increment 10 to an integer!
# 
# 1. Create the variable `startVal` with a value of 0. Create the variable `increment` with a value of 10.
# 2. Create a simple for loop (`for i in range...`) that repeats 10 times.
# 3. Inside the loop (indent), use either `+=` or `-=` to change the value of `startVal`
# 

# In[22]:



startVal = 0
increment = 10
for i in range(10):
    startVal+=10


# In[23]:


# run this cell to see what the final value of startVal is!
print(startVal)


# ## 4. Indexing multiple lists with a single for loop (intermediate)
# If you're programming with lots of lists, odds are you will want to work with more than one in a repeated fashion. Let's say you're going to update your turtle color using a list, and stamping it at a list of locations. You'll need two lists: `colors` and `locations`. `locations` is made for you.
# 
# In the cell below, create a list called `colors` that contains 'violet', 'green', and 'aquamarine'

# In[1]:


locations = [(100,100),(-50,76),(200,-87)] # this is a list of tuples...whoa...
colors = ["violet","green","aquamarine"]


# To step through the list of loops, we can use the `range()` function in combination with the built-in `len()` function, which returns the number of elements of a variable.

# Now we can use a for loop to generate an index, and us that index to access our lists. The loop below does this for `locations` only. Copy the last line of the loop and past it in line 9. Change the line so that we're using the `turtle.color()` function with the `colors`list. (*hint: colors[i] goes in the parentheses*)

# In[2]:


import turtle

turtle.up() # pick up pen
turtle.shape('turtle')
turtle.width(4) # thick line for easier visibility

for i in range(len(locations)):
    turtle.goto(locations[i])   # got to location in the list in each step of the loop
    print("The iteration is {}. The location is {}".format(i, locations[i]))
    # add line to change change color here
    turtle.color()
    turtle.stamp()    # stamp the turtle!
    
turtle.done()


# ## 5. Working with lists of mismatched lengths (advanced, optional)
# 
# Sometimes, we'll want to use a set of colors for a larger number of repeats. This is where the **modulo operator**  `%` comes into play.
# 
# **Modulo** returns the remainder of the number on the left divided by the number on the right:
# 
# `leftNum % rightNum --> Remainder`
# 
# We can set the length of our small list as the left number and our index variable as the right number. We can use this entire line to access a list from start to end, start to end, start to end... (In other words: color[0], color[1], color[2], color[0], color[1], color[2], and so forth)
# 
# `index % short list`
# 
# This way, as our index grows in the for loop, the remainder will cycle through values! That cycling will let us continually step through our short list. Let's give it a try!

# Let's start by making `locations` into a longer list. Use the append function that's built into lists to add 3 more values to the list. 
# You must add values one at a time. The first one is done for you.
# 
# Add the two tuples below:<br>
# `(90,-43)`<br>
# `(0,0)`

# In[ ]:


locations.append((-60,-100))
locations.append((-30,-130))
locations.append((-10,-150))

# in the lines below add the 2 other tuples using the append function
# note the parentheses inside the append function!


# Great! Now copy **only the for loop** (lines 6-10) from earlier and paste it below.<br>
# Change **line 8** so that the index for the list `colors` is: [i % colors]
# 
# **Remember: the formula to repeat colors  is `dataStructure[index variable % SHORTER dataStructure]`**

# In[6]:


for i in range(len(locations)):
    turtle.goto(locations[i])   # got to location in the list in each step of the loop
    print("The iteration is {}. The location is {}".format(i, locations[i]))
    # add line to change change color here
    turtle.color(colors[i])
    turtle.stamp()  
turtle.done()# stamp the turtle!


# # Check your answers
# Run the cell below to check your answers!

# In[ ]:


assert type(startVal)== int or type(startVal) == float, "startVal isn't a number. Check the definition in Section 3." 
assert startVal == -100 or startVal == 100, "Uh oh. Check that: increment = 0, startVal = 0 and you used range(10) in the for loop!"
assert len(locations) == 5, "You did not add the right number of elements to the locations list. Please try again."

print('Great job, programmer!')


# ## Thought project (expert)
#  
# ### How can we use modulo and RGB values to incrementally change a value?
# For this thought project, you may want to think about the assignment operators `+=` or `-=`. You can read about these here. 
# We'll use these in combination with for loops in the next workbook.
# 
# Hints:<br>
# `turtle.color((0,0,0)) # Black`<br>
# `turtle.color((50,50,50)) # Dark Gray`<br>
# `turtle.color((100,100,100)) # Lighter Gray`<br>
# What's the pattern here? Try to create a gradually darkening red color below using a for loop and RGB values.
# 
# 

# In[ ]:




