import requests
from bs4 import BeautifulSoup
import os
import time
from random import randint
from progress.bar import Bar
# bad words
listik_white = '1234567890'
listik_black = ':/\?*<>|'
#just words
spisok_answs = ['n', 'no', 'нет', 'н']
y = 0
spisok = ['glava-', 'epizod-']
#hello
print('Starting')

variable = 0
while variable == 0:
    try:
        q1 = int(input('Last downloaded chapter (if you didnt download any chapter, enter the first one)? \n Here: '))
        variable += 1
    except:
        print('You have done an mistake')

q3 = str(input('Type url \n Here: '))
#get way and url
direct = os.getcwd()
direct = str(direct)
#request
chet = 0
while chet == 0:
    try:
        reqs = requests.get(q3)
        chet = 1
    except:
        continue
soup = BeautifulSoup(reqs.text, 'lxml')
#get all urls
f = []
for link in soup.find_all('a'):
        with open('text.txt', 'a') as file:
            file.write(f"{link.get('href')}\n")
            for tu in spisok:
                if tu in link.get('href'):
                    f.append(link.get('href'))
                    y += 1
f.pop(0)
os.remove('text.txt')
#name of book
head_book = str(soup.find('h1', itemprop='name').text)
print(head_book)
#creating folder
for w in head_book: #create good name for file
    if w in listik_black:
        head_book = head_book.replace(w, '')
    else:
        continue
try:     
    os.mkdir(head_book)
except:
    pass
#limit
f1 = list(f)
f1 = len(f1)
q = q1
k = 1
i = q
i += 50
one = 0
print('\n[+]Doing')
#while 
bar = Bar('Processing', fill='-', suffix='%(percent).0f%%', max=50)
f2 = f1+1
while q != f2:
    count = 0
    if one != 0:
        if q == i:   #limit
            print('\n[+]Pause')
            if one != 0:
                chet = 0
                while chet != 30:
                    try:
                        sesin = requests.get(url=f[f1-q])
                        chet += 1
                        time.sleep(randint(1, 4))
                    except:
                        continue
            print('Go to site and solve "HCaptcha"')
            t = input('Continue?\n Here[y/n]: ')  #continue or stop
            if t in spisok_answs:
                print('\n[+]Stop')
                break
            else:
                print('Your answer is yes. Please, wait.')      
                i += 50
                bar.finish()
                bar = Bar('Processing', fill='-', suffix='%(percent).0f%%', max=50)
    one += 1
    chet = 0
    while chet == 0:
        try:
            res = requests.get(url=f[f1-q])  #page
            chet = 1
        except:
            continue
    soup1 = BeautifulSoup(res.text, 'lxml')
    enpty = soup1.find('div', class_='entry themeform').find_all('p') #content
    h = soup1.find('h1', class_='entry-title').text  #name chapter
    h = str(h)
    for c in enpty: #write content
        if count == 0:
            h = h.split(' ')
            h = '_'.join(h)
            for w in h: #create good name for file
                if w in listik_white:
                    continue
                else:
                    h = h.replace(w, ' ')
            h = h.split(' ')
            neq = 0
            spec = 0
            for ne in h:
                neq += 1
                for ino in ne:
                    if ino in listik_white:
                        h = h[neq-1]
                        spec += 1
                        break
                if spec == 1:
                    break
            future = h
            count += 1
            h = f'{direct}\\{head_book}\\{h}.txt'  #way for file with his name chapter
        try:
            with open(h, 'a', encoding='utf-8') as file: #open
                file.write(f'{c.text}\n') #write
        except OSError:
            pass
    j = randint(2, 5) #sleep
    time.sleep(j)
    q += 1
    bar.next()
    # print(f'Downloaded {future} chapter ')
print('Goodbye')
bar.finish() 