import pymysql
from tkinter import *
import pyttsx3
import datetime
import random
import tkinter as tk
from bs4 import BeautifulSoup
import urllib.parse
import os
import os.path
import cv2
from urllib.request import Request,urlopen
#import  speech_recognition as sr
import nltk
from nltk.corpus import wordnet
goku = pyttsx3.init()
goku.setProperty('rate', 150)
goku.setProperty('volume', 9)
marvel =Tk()
marvel.title('Caffy')
v = StringVar()
ne = tk.Text(marvel, height=10, width=100)
dir ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drv = ['%s:'% d for d in dir if os.path.exists('%s:' % d)]
j=90
#nltk.download()
def ts():
    home()
    eee.place(relx=0.3, rely=0.1)
    bt.place(relx=0.58, rely=0.1)
def ts1():
    a = eee.get()
    a=a.lower()
    eee.delete(0, 'end')
    db = pymysql.connect(host='localhost', user='root', password='@Python123', db='talk')
    cur = db.cursor()
    sq = ("""select ans from chat where ques like""" + "'" + "%" + a + "%" + "'")
    cur.execute(sq)
    dat = cur.fetchone()
    a = str(dat).strip('[]()'',')
    goku.say(a)
    goku.runAndWait()
def news():
    home()
    ne.delete('1.0', END)
    jv = 'https://www.deccanchronicle.com/'
    gf = urllib.request.urlopen(jv)
    bf = BeautifulSoup(gf, 'html.parser')
    tv = bf.find('div', attrs={'class': 'col-sm-5 tsSmall'})
    na = tv.text.strip()
    na = na.strip()
    ne.place(relx=0.3, rely=0.1)
    ne.insert(tk.END, na)
def score():
    home()
    ne.delete('1.0', END)
    jv = Request('https://www.cricbuzz.com/cricket-match/live-scores/recent-matches', headers={"User-Agent": "Mozilla/5.0"})
    gf = urlopen(jv)
    bf = BeautifulSoup(gf, 'html.parser')
    for i in bf.findAll('div', attrs={'class': 'cb-lv-scrs-col text-black'}):
        na = i.text.strip()
        print(na)
    tv = bf.find('div', attrs={'class': 'cb-scr-wll-chvrn'})
    na = tv.text.strip()
    ne.place(relx=0.3, rely=0.1)
    ne.insert(tk.END, na)
def proverb():
    home()
    ne.delete('1.0', END)
    pdict = dict(
        {1: 'look before you leap', 2: 'face s the index of mind', 3: 'accept the change that you cannot change it',
         3: 'follow your dreams', 4: 'a friend is a friend indeed',
         5: 'changes is the only thing that cannot change'})
    sk = random.randrange(1, 6)
    ne.place(relx=0.3, rely=0.1)
    ne.insert(tk.END, pdict[sk])
def joke():
    home()
    ne.delete('1.0', END)
    remo = random.randrange(1, 4)
    gdict = dict({
        1: 'A man wears a green shirt and rides on a royalenfield and suddenly get downs and knock the door of the house you know why,because the door bell not work',
        2: 'joke over',
        3: 'Can a kangaroo jump higher than a house?ofcourse the house cannot jump',
        4: 'A man addicted to a twitter and ask him for a solution,doctor said sorry i dont follow you'})
    ne.place(relx=0.3, rely=0.1)
    ne.insert(tk.END, gdict[remo])
def open():
    home()
    eee.place(relx=0.3, rely=0.1)
    bto.place(relx=0.58, rely=0.1)

def op():
    global fu,liss
    #eee.delete(0, 'end')
    a=eee.get()
    print(a,"df")
    eee.delete(0, 'end')
    fu=[]
    liss=[]
    for dr in drv:
        for root, dirs, files in os.walk(dr):
            for file in files:
                s=file
                if s.find(a) == -1:
                    pass
                else:
                    for file in root:
                        i = os.path.join(root, s)
                        fu.append(s)
                        liss.append(i)
                        break
    print(a,fu)

    lb.place(relx=0.3, rely=0.1)
    lb.delete(0, 'end')
    for it in fu:
        lb.insert(END, it)

def selg(evt):
    global fu, liss
    value = str((lb.get(lb.curselection())))
    f = fu.index(value)
    os.startfile(liss[f])
def syn():
    home()
    ne.delete('1.0', END)
    eee.delete(0, 'end')
    eee.place(relx=0.3, rely=0.1)
    bts.place(relx=0.58, rely=0.1)
def syn1():
    home()
    tamil = eee.get()
    y = wordnet.synsets(tamil)
    ne.place(relx=0.3, rely=0.1)
    ne.insert(tk.END, y[0].definition())
def snap():
    home()
    p = str(datetime.datetime.now())
    pp = [i for i in p if i.isdigit()]
    pr = "".join(pp)
    name =drv[-1] + str(pr)+".png"
    gu = cv2.VideoCapture(0)
    ret, frame = gu.read()
    cv2.imwrite(name, frame)
    gu.release()
    cv2.destroyAllWindows()
    os.startfile(name)
def pong():
    os.system('python singleplayer.py')


def home():
    ne.place_forget()
    bto.place_forget()
    lb.place_forget()
    eee.place_forget()
    bt.place_forget()
    bts.place_forget()
    return




eee = Entry(marvel, textvariable=v, width=70)
bt = Button(marvel, text="Go", command=ts1)
bto = Button(marvel, text="Go", command=op)
bts = Button(marvel, text="Get", command=syn1)
lb=Listbox(marvel,width=60,height=10,font=('times',13))
lb.bind('<<ListboxSelect>>',selg)
button=Button(marvel,text="Chat",command=ts,width=30,height=5).place(relx=0.2,rely=0.4)
button=Button(marvel,text="News",command=news,width=30,height=5).place(relx=0.4,rely=0.4)
button=Button(marvel,text="Score",command=score,width=30,height=5).place(relx=0.6,rely=0.4)
button=Button(marvel,text="Proverb",command=proverb,width=30,height=5).place(relx=0.2,rely=0.5)
button=Button(marvel,text="Joke",command=joke,width=30,height=5).place(relx=0.4,rely=0.5)
button=Button(marvel,text="Open",command=open,width=30,height=5).place(relx=0.6,rely=0.5)
button=Button(marvel,text="Synonyms",command=syn,width=30,height=5).place(relx=0.2,rely=0.6)
button=Button(marvel,text="Home",command=home,width=30,height=5).place(relx=0.4,rely=0.6)
button=Button(marvel,text="selfie",command=snap,width=30,height=5).place(relx=0.6,rely=0.6)
button=Button(marvel,text="pingpong",command=pong,width=30,height=5).place(relx=0.4,rely=0.7)
mainloop()