import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# Authenticate using creds.json
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the spreadsheet
sheet = client.open("Automation_Spreadsheet").sheet1

# Collects user responses
personal_list = []

print("Hi! I just noticed you and I hope you are doing well.")

input("How are you doing today?: ")

print("Ok, great!")

# First Question
first_question = input("Now tell me what is your favorite color?: ")
personal_list.append(first_question)

# Second Question
second_question = int(input("Tell me a random number: "))
print("Thank you!")
personal_list.append(second_question * 10) # multiplied by 10

# Third Question (multiple parts)
name = input("Now, tell me your name, your phone number, your age, and your email adress so I can save it in my local files (Start with name): ")
phone_number = input("Tell me your phone number: ")
age = int(input("Tell me your age: "))
email = input("Finally, tell me your email adress: ")

# Person class
class my_person:
    is_adult = False
    def __init__(self, name, phone_number, age,  email):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.email = email

    @classmethod
    def if_adult(cls, age):
        if age >= 18:
            cls.is_adult = True

    def display_person(self):
        print(f"This person is called {self.name}, their age is {self.age}, their phone number is {self.phone_number}, and their email is {self.email}. Pretty Cool!")

# Create and display the person
person = my_person(name, phone_number, age, email)
person.display_person()

# Update the Google Sheet
next_row = len(sheet.get_all_values()) + 1

person_row = [person.name, person.phone_number, person.age, person.email,]

update_sheets_range = f"A{next_row}:D{next_row}"

sheet.update(update_sheets_range, [person_row])