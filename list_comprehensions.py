#!/usr/bin/env python
# coding: utf-8

# In[2]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    


# In[4]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits


# In[51]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.capitalize() 
                      for fruit in fruits]

capitalized_fruits


# In[50]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruit1 = 'guava'
len([letter 
     for letter in fruit1 
     if letter in 'aeiou'])


# In[20]:



fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou']) > 2]


# In[21]:


fruits_with_more_than_two_vowels


# In[23]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

[fruit 
 for fruit in fruits 
 if len([letter for letter in fruit if letter in 'aeiou']) == 2]



# In[31]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters


[fruit 
 for fruit in fruits 
 if len(fruit) > 5]


# In[33]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters


[fruit 
 for fruit in fruits 
 if len(fruit) == 5]


# In[54]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters


[fruit
 for fruit in fruits 
 if len(fruit) <5]


# In[43]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

numbers




# In[44]:


[len(fruit) 
 for fruit in fruits]


# In[47]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit 
                        for fruit in fruits 
                        if 'a' in fruit]




# In[48]:


fruits_with_letter_a


# In[66]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 



fruits_with_letter_a = [num 
 for num in numbers 
 if num % 2 == 0]


# In[55]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers


odd_numbers = [num 
 for num in numbers 
 if num % 2 == 1]


# In[56]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [num 
 for num in numbers 
 if num > 0]


# In[65]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers


negative_numbers = [num 
 for num in numbers 
 if num < 0]


# In[67]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

[num 
 for num in numbers 
 if not (-10 < num < 10)]




# In[91]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [num ** 2 for num in numbers]




# In[79]:


numbers_squared


# In[80]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [num for num in numbers if num < 0 and num % 2 == 1]




# In[81]:


odd_negative_numbers


# In[82]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = [num + 5
                   for num in numbers]




# In[83]:


numbers_plus_5


# In[ ]:




