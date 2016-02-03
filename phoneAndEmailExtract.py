#! python3
#phoneAndEmailExtract.py -Phone Number and Email Extractor

import re, pyperclip

#create phoneRegex
phoneRegex = re.compile(r'''
    (
    (\d{3}|\(\d{3}\))?              #area code: 0-1 of xxx or (xxx)
    (\s|-|\.)                       #separator: space or - or .
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separator: same as before
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension: 0-1 of space(0+), ext or x or ext., then space and 2-5 digits 
    )''', re.VERBOSE)

#create emailRegex
emailRegex = re.compile(r'''
    (
    \w+                             #username
    @                               #@ symbol
    [a-zA-Z0-9.-]+                  #domain name
    (\.[a-zA-Z]{2,4})               #dot-something
    )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
