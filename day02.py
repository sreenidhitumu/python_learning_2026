#strings

#basic string operations
name="Baraa"
print(type(name))
age=30
print("your name is " + name)
print("your age is " + str(age)) #convert into string

# len function
password="123a"
print(len(password))
if len(password) < 8:
    print("Your password is too short")

#count the occurrence of a string
text="""
Python is easy
Python is powerful
"""
print(text.count("Python")) #counts occurrence of Python case sensitive

#replace method
price="123,456"
print(price.replace(",","."))

phone="176-1234-56"
print(phone.replace("-","")) #replace with nothing

price="$1,299.99"
price=price.replace("$","").replace(",","") #chained methods are executed from left to right
price=float(price)
print(type(price),price)

#convert "+49 (176) 123-4567" into a clean number format with only digits
phone = "+49 (176) 123-4567" 
phone = phone.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ","")
print(phone)

#concatenate
first_name="Michael"
last_name="Scott"
name = first_name + " " + last_name
print(name)

# #f-string formatted string
name = "Sam"
age = 34
is_student = False
print("My name is " + name + ",I am " + str(age) + " years old") #convert into string
print(f"My name is {name} and my age is {age} and status is {is_student}") #converts all data types into string
print(f"2 + 3 = {2+3}") #can add expressions also
print(f"{{This is me}}") #to print the curly brackets

#split method
stamp = "2026-09-20,USA,SAM,Kentucky"
print(stamp.split(",")) #values separated into a list

#multiplier
print("ha"*3)
print("=" * 30)

#indexes and slicing
text = "Python"
print(text[0:5]) #character on 5 is not included
print(text[0:]) #till the end
print(text[0:6:2]) #start:stop:step take every 2nd character starting from 1st

#cleaning string values
text=" Engineering " 
text=" Engineering ".lstrip() #removes left space
print(len(text))
print(len(text.strip())) #detect white space
number_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print(number_of_spaces, is_clean)


text = " Engineering ".rstrip() #removes right space
print(text)
text="Data Engineering".strip() #strip does not remove spaces in between
print(text)

text="###ABC###".strip("#") #remove a special character
print(text)

#case conversions
text="PYThOn"
print(text.lower()) #lower case
print(text.upper()) #upper case

#find a specific term in any case
search = " Email".lower().strip() #clean - convert into lower and remove whitespaces
data = "emAil".lower().strip()
print(search==data)

#clean the messy string
string = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
name = string[4:9]
print(name)
role = string[13:26].replace("@","a")
print(role)
age = string.strip()[-3:-1]
print(f"name: {name} | role: {role} | age: {age}")