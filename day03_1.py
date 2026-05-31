#string functions searching

date = "2026-Feb-10"
print(date.find("Feb")) #finds the character start location
print(date.startswith("2026")) #startswith
file="data_backup.csv"
print(file.endswith("csv")) #endswith
email = "tumu@gmail.com"
print("@" in email) #check if @ is present in email

url = "https://api.company.com"
print("/api" in url)

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
print(phone1[4:])
print(phone2[3:])

print(phone1.find("-"))
print(phone1[phone1.find("-")+1:]) #find the number without counting
print(phone2[phone2.find("-")+1:])

#string validating
country="USA1"
print(country.isalpha()) #checks if string has only letters

number = "098938 448943"
print(number.isnumeric()) #checks if string has only numbers; special characters not validated