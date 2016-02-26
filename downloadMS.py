#! python3
# downloadMS.py -Downloads manga pages from (url) to (endurl) on www.mangastream.to.

import os, requests, bs4, sys

#function for when program is run in the command line
def execute_standalone():
    global url, endurl, fname
    url = sys.argv[1]
    endurl = sys.argv[2]
    fname = sys.argv[3]

#main

#If program is run in IDLE shell
if 'idlelib.run' in sys.modules:
    print('Type the url of the first manga/webcomic page to download.')
    url = input()

    print('Enter name of destination folder')
    fname = input()

    print('Type the url of the last manga/webcomic page to download.')
    endurl = input()  
    
#Otherwise assume program is run from command line
else:
    execute_standalone()

#Make folder named fname if it does not exist already
fname = 'C:/Insert/Existing/Folder/Destination/' + fname    
os.makedirs(fname, exist_ok=True) 

while not url.endswith(endurl): #while the endurl has not been reached
    stripUrl = url.rsplit('-', 4) #split the url based on hyphens and store in list stripUrl
    chapterUrl = fname + '/' + stripUrl[1] + stripUrl[2] #use the chapter name and number extracted from the list stripUrl
    os.makedirs(chapterUrl, exist_ok=True) #make chapter folder if it does not exist already
    #Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #Find the URL of the comic image.
    comicElem = soup.select('#page-content img')
    if comicElem == []:
        print('Could not find image.')
    else:
        try:
            comicUrl = comicElem[0].get('src')
            #Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
           
            nextLink = soup.select('#page-content a')[0]
            if len(nextLink.get('href')) > 9:
                url = 'http://www.mangastream.to' + nextLink.get('href')
            else:
                url = stripUrl[0] + '/' + stripUrl[1] + '/' + nextLink.get('href')
            continue
 

    #Save the image to chapter folder.
        imageFile = open(os.path.join(chapterUrl, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    #Get the next page's url.

        nextLink = soup.select('#page-content a')[0]
        if len(nextLink.get('href')) > 9:
            url = 'http://www.mangastream.to' + nextLink.get('href')
        else:
            url = stripUrl[0] + '/' + stripUrl[1] + '/' + nextLink.get('href')


print('Done.')
