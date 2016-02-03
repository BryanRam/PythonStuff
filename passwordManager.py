#! python3
#passwordManager.py - A slightly more secure password manager, using shelve variables
import sys, pyperclip, shelve, os

shelfFile = shelve.open(os.path.abspath(r'Path\To\Target\Shelf\file'))

#adds a new account with corresponding password, or edits already existing account's password
def addPass(username, pswd):
    shelfFile[username] = str(pswd)
    print('Password for ' + username + ' added')

#copies [username]'s password to clipboard 
def getPass(username):
    if username in shelfFile:
        pyperclip.copy(shelfFile[username])
        print('Password for ' + username + ' copied to clipboard.')
    else:
        print('There is no account named ' + username)
    

#main
if len(sys.argv) < 2:
    print('Usage: python passwordManager.py [account] - copy account password')
    print('       python passwordManager.py [account] [password] - add/edit account')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if len(sys.argv) == 3:
    addPass(account, sys.argv[2])

if len(sys.argv) == 2:
    getPass(account)



shelfFile.close()
