#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lambda function
# Map function
# Filter function


# In[20]:


#LAMBDA

#Normal functions are defined using the keyword in Python, Anonymous functions are defined using the lambda keyword.

# So essentially anonymous functions are also called lambda functions.
#Anonymous functions are functions without a keyword.

# We can pass arguments to the lambda using args and kwargs.
# Args: The Non-keyword arguments (Args = Arguments)
# Kwargs: The keyword argument  (Kwargs = Keyword Arguments)


# In[13]:


def div (x,y):
    return x/y
print (div(8,2))
# Instead of using the above to define a function, we can define a function using lambda as seen below:
divd = lambda g,h : g/h
print (divd(8,2))
#This function divides the value of "g" by the value of "h"


# In[14]:


addi = lambda a : a + 7
a = 3
print (addi(a))
# This functions adds 7 to the value of "a"


# In[15]:


def multply (one_list):
    result = 1
    for elements in one_list:
        result = result * elements
    return result

bingo = [3,5,6]
multply (bingo)
# The conventional way of multiplying all the elements in a list


# In[19]:


def multiply (*args):
    result = 1
    for elements in args:
        result = result * elements
    return result

multiply (3,5,6)
# The Pythonic way of multiplying elements. NOTE: you don't need to create a list to use this method.
# Here we can input as many elements as we want.


# In[31]:


def display (**kwargs):
    for k,v in zip (kwargs.keys(), kwargs.values()):
        print (k,v)
        
print (display (Imo = "Owerri", Abia = "Umuahia", Anambra = "Awka" ))
# Pythonic way of displaying dictionaries

bin = {"Im" : "Owerri", "ab" : "umuahia"}
print (bin)
# Conventional way of displaying dictionaries


# In[45]:


# To convert a list, set, dictionary to an iterator
list_1 = [2,5,1,6,8]
iterator = iter(list_1)
#NOTE: We cannot print the iterators. We can only call one at a time using the next function. As seen below. 


# In[37]:


print (next(iterator))


# In[46]:


#Generators are the functions we use to create iterators
# Yield is the difference between regular functions and generators


# In[58]:


def reverse (data):
    for i in range(len(data) -1,-1, -1):
        print (data[i])
reverse (list_1)


# In[64]:


def reverse (data):
    reverse_list = []
    for i in range(len(data) -1,-1, -1):
        reverse_list.append(data[i])
    return reverse_list
reverse (list_1)


# In[86]:


def reverse_generator (data):
    for i in range(len(data) -1,-1, -1):
        yield data[i]
#Using generators to return a reverse of the list


# In[87]:


reverse_generator_list = reverse_generator(list_1)


# In[88]:


print (next(reverse_generator_list))
# Note: When using generator, it continues the code from the last element. 
# The "next" function is used to print one element at a time


# In[89]:


for i in reverse_generator_list:
    print (i)
# Using the For loop prints/ displays the entire element at once. 
#Note: It continues from the last element ("8" is not included, since it has already been printed above using the next function)


# In[8]:


def add_two(a_list):
    result = []
    for element in a_list:
        element+=2
        result.append(element)
    return result
hat = [8,5,2,5]
add_two (hat)
#Conventional way of adding two to the elements in a lists


# In[58]:


# Map: takes at least two arguments. The first is the function, the second is the value to which we will apply the function to.
def add_two_map (element):
    return element + 2
result_map = map(add_two_map, hat)
#Uses map to add two to the elements in a list. Note: We are using map in a conventional way


# In[59]:


type (result_map)


# In[60]:


next(result_map)


# In[61]:


next(result_map)


# In[62]:


#To convert a map back to a list, we use the list function
list(result_map)


# In[77]:


#Let's use map function in a pythonic way by using the lambda function
result_map_lambda = map( lambda element: element+2, hat)


# In[64]:


result_map_lambda_list = list (result_map_lambda)


# In[65]:


pow (8,2)
#the power function. takes to argument. the base and the power. 


# In[86]:


pow_list = [2,5,2,3]
pow_map_list = map (pow, result_map_lambda_list, pow_list)
#Using pow function in map


# In[87]:


list(pow_map_list)


# In[69]:


pow_map_list_1 = map (pow, hat, pow_list)


# In[70]:


list(pow_map_list_1)


# In[119]:


input_list = ['What we think, we become.', 'Every moment is a fresh beginning.', 'Change the world by being yourself.',
             'Hate comes from intimidation, love comes from appreciation', 'If I’m gonna tell a real story, I’m gonna start with my name.', 'Oh, the things you can find, if you don’t stay behind.']
result = 0
for element in input_list:
    count = element.count('n')
    result = result + count
print(result)


# In[124]:


mapped_list = map(lambda element : element.count('n'), input_list)


# In[125]:


list (mapped_list)


# In[139]:


mapped_list_1 = list (map (lambda element : element.count("n"), input_list))


# In[140]:


print (mapped_list_1)


# In[141]:


for element in mapped_list_1:
    if element>2:
        print (element)


# In[146]:


def above_two (number):
    result = []
    for element in number:
        if element > 2:
            result.append(element)
    return result
above_two (mapped_list_1)
#Conventional method. 


# In[151]:


# The filter function needs a function that returns True or False
def above_two_filter (numbers):
    return numbers > 2
above_two_filter_list = list(filter(greater_than_two, mapped_list_1))
print (above_two_filter_list)
#The filter is used to filter out the elements in the list, set, tuple etc based on a certain criteria


# In[154]:


# Using the pythonic method and reducing the lines and memory.
above_two_pythonic = list (filter (lambda numbers : numbers > 2, mapped_list_1))
print (above_two_pythonic)


# In[168]:


#Question: Print only even Numbers.
#Method 1: Conventional Method
list_quiz = [ 120 , 31 , 19 , 28 , 512 , 957 , 6321 ]
result = []
for element in list_quiz:
    if element%2 == 0:
        result.append(element)
print (result)


# In[169]:


#Method 2: Using filter with defining function. Shorter than the conventional method
def list_quiz_filter(element):
    return element%2 == 0
ddk = list (filter (list_quiz_filter, list_quiz)) 
ddk


# In[170]:


#Method 3: Using filter with lambda. The shortest method.
list_even = list (filter( lambda element: element%2==0, list_quiz))
print (list_even)


# In[ ]:





# In[ ]:




