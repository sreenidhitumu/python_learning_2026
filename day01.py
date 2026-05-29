
#Variables - print the following
#info@datawithbaraa.com
#support@datawithbaraa.com
#www.datawithbaraa.com
#print function
temp="datawithbaraa.com"
print("info@",temp, sep="") #changing the separator
print("support@"+temp) #using string concatenation
print(f"www.{temp}") #using f-string

#input function - to get user input
name = input("Enter your name")
print(name)

#variables data types and length
age=25
height=150.5
name="Python"
Student=False
novalue=None

print(age, type(age), age.bit_length())
print(height, type(height))
print(name, type(name), len(name))
print(Student, type(Student))
print(novalue, type(novalue))