#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') #display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)


#Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = len(linkElems)
counter = 5

for i in range(counter):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

if numOpen > 5:
    print('Continue? Y/N')
    answer = input()
    if answer.lower() == 'y' or answer.lower() == 'yes':
        for i in range(counter,min(counter+4,numOpen)):
            webbrowser.open('http://google.com' + linkElems[i].get('href'))
