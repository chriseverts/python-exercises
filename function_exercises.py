##1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two (x):
    if x == 2:
        result = True
    else: 
         result = False
    return result
    


##2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.


def is_vowel(string):
    
    return string.lower() in "aeiou"
string = "U"

is_vowel(string)



def is_vow(string):
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
def capword(user):
    if user[0] not in 'aeious':
        user = user.capitalize()
    return(user)

    



##5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(bill, tip_percent):
    
    return bill * tip_percent
bill = 40
tip_percent = .30

calculate_tip(bill, tip_percent)

        
##6. Define a function named apply_discount. 
# It should accept a original price, and a discount percentage,
#  and return the price after the discount is applied.


def apply_discount(a,b):
    discount = b - a
    dispercent = (discount/b) *100
    total_price = (b * dispercent) - b
    return total_price

##7Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.

def handle_commas(b):
    return float(b.replace(",", ""))


##8. Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    
    if number <= 69:
    
        grade = "F"
    
    elif number <= 79:

        grade = "C"

    elif number <= 89:

        grade = "B"

    else:

        grade = "A"

    return grade
        
##9. Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.


string = input("Enter any string: ")
def remove_vowels(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr
remove_vowels(string)


##10 Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:

def remove_symbols(name):
    cleaned = ""
    for char in name:
                if (char.isalnum() == True) or (char ==" "):
                    cleaned += char
    return cleaned


##11.Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
##cumulative_sum([1, 1, 1]) returns [1, 2, 3]
##cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# cumulative_sum is a single parameter, lists is a string, will return a cumulative list
def cumulative_sum(lists):
    cu_list = []
    length = len(lists)   # length is the length of the lists which is a paramter
    cu_list = sum(lists[0:x:1]) # sums the list of integers in the parameter
    for x in range(0, length+1): 
            return cu_list[1:] # returns the new list