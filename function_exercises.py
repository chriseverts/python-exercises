##1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two (x):
    if x == 2:
        result = True
    else: 
         result = False
    return result
    


##2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    for char in string:
        if char.lower() in 'aeiou':
            return True
    return False

##3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.   

def is_consonant(string):
    for char in string:
        if char.lower() not in 'aeiou':
            return True
        return False





        
