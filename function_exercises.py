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



##4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

user = input("Please enter a sentance")

print(user.title())



##5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculateTip(total_cost,tip):
        total_cost = 20
        tip = 1  
        new_total = (total_cost * tip) / 100 + total_cost
        return new_total

        
