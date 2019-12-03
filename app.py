print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

number_value = 345.43543
is_male = True

print("Giraffe\nAcademy\"")
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0] + phrase[3])
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))

print(2)
print(2.09389)
print(-2.435)
print(3*4+5)
print(3*(4+5))
print(10%3)#remainder
my_num = 5
print(my_num)
print(str(my_num) + " my favorite number")#convert to string
my_num = -5
print(abs(my_num))#absolute value
print(pow(3, 2))#3 to the power of 2
print(min(4, 6))#prints smallest number
print(max(4, 6))#prints largest number
print(round(3.2))#rounds number
from math import *   #imports various math functions
print(floor(3.7))#rounds down
print(ceil(3.1))#rounds up
print(sqrt(36))#finds the square root

#name = input("Enter your name: ") #variable name is whatever is in input
#age = input("Enter your age: ")
#print("Hello " + name + "! You are: " + age)

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")#num1 and num2 are currently strings, must convert to floats for calculations
#result = float(num1) + float(num2)
#print(result)

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tammy", "Bobby"]
#             0        1       2
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[1] = "Mike"
print(friends[1])

lucky_numbers = [4, 15, 8, 42, 23, 16]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Tammy", "Bobby"]
#friends.extend(lucky_numbers)#add two lists together
#friends.append("Creed")#add an item onto the list
#friends.insert(1, "Kelly")
#friends.remove("Jim")
#friends.clear#clear list
friends.pop #'pop' the last element off of the list
print(friends)
print(friends.index("Kevin"))
print(friends.count("Oscar"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)

#tupple (is immutable - cannot be modified once created)
coordinates = (4, 5)
print(coordinates[0])


#functions
def say_hi(name, age):
    print("Hello " + name + " you are " + age)
print("top")
say_hi("Mike", "26")
print("bottom")
say_hi("Steve", "70")

def sayhi(name, age):
    print("Hello " + name + " you're " + str(age))
sayhi("Bob", 44)

def cube(num):
    return num*num*num   #return is what gives the value (return ends the function - cannot print return w/in function)

result = cube(4)
print(result)


is_male = True
is_tall = False
if is_male:
    print("You are male.")
else:
    print("You are female.")

if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")

if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall.")

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are a tall female.")
else:
    print("You are a short female.")


#==  equal to
#!=  not equal to
#can also compare strings
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(34, 564, 467))


#num1 = float(input("Enter first number: "))
#op = input("Enter the operator: ")
#num2 = float(input("Enter second number: "))
#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "*":
#    print(num1 * num2)
#elif op == "/":
#    print(num1 / num2)
#else:
#    print("Invalid operator")


#Dictionaries - key/value pairs (word is the key, value is definition)
#keys must be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Pan"))
print(monthConversions.get("Luv", "Not a valid key."))


#while loops
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop.")


#guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#    else:
#        out_of_guesses = True
#
#if out_of_guesses:
#    print("Out of guesses, YOU LOSE")
#else:
#    print("You win!")


#for loop of array
friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)
print(len(friends))
for index in range(len(friends)):
    print(friends[index])

for letter in "Giraffe Academy":
    print(letter)

for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")


#exponent function (take a number and raise it to a power
print(2**3)

#function where base_num is raised to power_num
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))


#2d lists and nested loops
#each item in the number grid list is another list (4 rows, 3 columns)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#print row 2, column 0 - or third row, first column as it is a base 0
print(number_grid[2][0])

#nested for loop
for row in number_grid:
    print(row)
for row in number_grid:
    for col in row:
        print(col)


#build a translator function (in this case, turns vowels into x)
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation
#print(translate(input("Enter a phrase:  ")))


#Comments in python
print("comments can be fun")
'''
This is how you can make multiple line comments,
but the super official people think you should
only ever use the hashtag.
'''


#Try Except (catching errors)
#must enter a number, then is converted into an integer, entering letters throws an error
'''number = int(input("Enter a number: "))
print(number)

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
'''
#can also put in specific exceptions to catch specific errors
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  #you can also have it print the error
    print(err)
except ValueError:
    print("Invalid input")


#Reading Files (reading from external files) - read command
#r for read, w for write, r+ is reading and writing
panda_file = open("panda.txt", "r")
#print file after checking it is readable
print(panda_file.readable)
print(panda_file.readline())
#put the lines in the file into a list
print(panda_file.readlines())
#can print each item in list
for panda_fact in panda_file.readlines():
    print(panda_fact)
#close file
panda_file.close()

#Writing to files
#a is for adding text onto the end of a file
panda_file = open("panda.txt", "a")
#panda_file.write("\npandas are sad bears")
panda_file.close()

#can create a new file - even create an html or something similar
'''
employee_file = open("employee.txt", "w")
employee_file.write("\nBob - First Hire")
employee_file.close()
'''



#Modules and Pip
#can import the useful_tools file to grab functions and info from there
import useful_tools
print(useful_tools.roll_dice(10))
#can import functionality from external files

#can find a list of python modules online that anyone can access (python.org)
#many external files are stored in Lib folder in External Libraries

#pip is a program you can use to install python modules (referred to as a package manager)
#can use command prompt and use pip (if python is installed should have it)
#pip install nameofpythonmodulehere
#module should then appear inside of site-packages file in Lib in External Libraries
#can also uninstall with pip uninstall nameofpythonmodulehere



#Classes and Objects
#not all info or data can be comprised of strings, booleans, or ints
#can create your own data type in the form of a class

#here i am importing the Student class from Student.py
from Student import Student
#after creating the class in the other file, now I am creating the object in this file
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.name)
print(student2.gpa)



#Building a multiple choice quiz
'''
#call the class for Question from Question.py
from Question import Question

#array for question prompts
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#create question objects
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
'''



#Object Functions
student3 = Student("Oscar", "Accounting", 3.1, False)
student4 = Student("Phyllis", "Business", 3.8, False)
#have previously called Student from Student (from Student import Student)
print(student3.on_honor_roll())
print(student4.on_honor_roll())



#Inheritance
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()




#Python Interpreter
#can open with command prompt
#may need to download python3 or research how to open python3 in cmd if on windows
#can then write python in cmd
#mostly just a place to test out python code "quick and dirty"