#A program to show how to validate user input using regex
import re

def validatePass(text):
    digits = '\d+'
    chars = r'\w+'
    passwordRegex = re.compile(r'(?=.*\d).{8,}')
    mo = passwordRegex.search(text)
    return mo


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break #exit while loop because valid age was entered
    print('Please enter a number for your age.')

while True:
    print('Select a new password.')
    print('Password must be at least 8 characters long and contain letters and numbers only:')
    password = input()
    result = validatePass(password)
    if result is None:
        print('Invalid password entered. Please try again')
        continue
    else:
        break

print('Password updated successfully')
