## 1. Conditional Basics








####prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = input("Please enter the day of the week")

if day_of_week.startswith("Mon"):
    print("That day is monday!")
else:
    print("That day is not monday!")

##prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input("Please enter the day of the week")

if day_of_week.lower().startswith("s"):
    print("{day_of_week}is a weekend day!")
else:
    print("{day_of_week} is not a weekend day!")




##create variables and make up values for the number of hours worked in one week
##the hourly rate
##how much the week's paycheck will be
##write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hourly_rate = 25
hours_per_week = 60

if hours_per_week > 40:
    overtime_h = hourly_rate - 40
    overtime_p = overtime_h + hourly_rate * .5
else 
    overtime_p = 0


paycheck = hourly_rate * hours_per_week + overtime_p

paycheck




##2 Loop Basics

##While

##Create an integer variable i with a value of 5.
##Create a while loop that runs so long as i is less than or equal to 15
##Each loop iteration, output the current value of i, then increment i by one.




i = 5
while i <= 15:
    print(i)
    i += 1


##Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2


##Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

## Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:


i = 2
while i <= 1_000_000:
    print(i)
    i = i ** 2


##Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

x = (input("Please enter a number:"))

for i in range(1, 11):  
        print("{x} x {i} = {x * i}")


##Create a for loop that uses print to create the output shown below.

for i in range(10):
    print(str(i) * i)


## Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.


n = input(" enter an odd number between 1 and 50")


for num in range(50):
    if num % 2 == 0:
        break
    print("Number must be odd")
    
n = input(" enter an odd number between 1 and 50")

while num in range(50):
    if num % 2 == 0:
        continue
    print(f'Here is an odd number: {num}')
    print(f'yikes skipping {num}')
    



    

    
