from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter.scrolledtext as scrolledtext
from PIL import ImageTk, Image
import sqlite3 
from random import randint
from bs4 import BeautifulSoup
import requests
import socket
import datetime
import webbrowser
import pyttsx3
import time
import wikipedia
import subprocess
import googlesearch	
import os,sys,making_dir



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

path = resource_path('images/')
window = Tk()
window.iconbitmap(path+'Icon.ico')

SEARCH=StringVar()
optionVar = StringVar()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def speak(audio):

    
    engine.say(audio)
    
    engine.runAndWait()
    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def database():
 
    #Function For Database Connectivity

    global conn, cursor #Making conn,cursor a globle variable

    conn = sqlite3.connect("C:\PyHelp\\history.db")#connecting to database

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS `history` (s_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Type TEXT, Date TEXT, Query Text)")
   
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Exit():
    result = tkMessageBox.askquestion(
        'PyHelp Search Engine', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        window.destroy()
        exit()

    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the application screen')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Home():
    
    global home
    home = Toplevel()
    home.title('PyHelp Search Engine')
    home.iconbitmap(path+'Icon.ico')
    home.resizable(0, 0)
    img = Image.open(path+"Home.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(home, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    search = Entry(home, textvariable=SEARCH, font=('arialnarrow', 24), width=34, bg="PaleTurquoise", borderwidth=5, relief = 'solid')
    search.place(x=275,y=35)

    
    lbl_txt1 = Label(home, text='''As A Programmer Let's
 Customize  search. Use-''', font=('Agency FB', 18),bg='white')
    lbl_txt1.place(x=7,y=120)
    lbl_txt2 = Label(home, text=''' • Lib:''', font=('Agency FB', 18, 'bold'),bg='white')
    lbl_txt2.place(x=7,y=177)
    lbl_txt3 = Label(home, text=''' <Your Query>''', font=('Agency FB', 18),bg='white')
    lbl_txt3.place(x=67,y=180)
    lbl_txt4 = Label(home, text='''     To Search For Any Library''', font=('Agency FB', 15),bg='white')
    lbl_txt4.place(x=7,y=210)
    lbl_txt5= Label(home, text=''' • Err:''', font=('Agency FB', 18, 'bold'),bg='white')
    lbl_txt5.place(x=7,y=235)
    lbl_txt6 = Label(home, text=''' <Your Query>''', font=('Agency FB', 18),bg='white')
    lbl_txt6.place(x=77,y=240)
    lbl_txt7 = Label(home, text='''     To Search For Any Error''', font=('Agency FB', 15),bg='white')
    lbl_txt7.place(x=7,y=270)
    lbl_txt8= Label(home, text=''' • Git:''', font=('Agency FB', 18, 'bold'),bg='white')
    lbl_txt8.place(x=7,y=295)
    lbl_txt9= Label(home, text=''' <Your Query>''', font=('Agency FB', 18),bg='white')
    lbl_txt9.place(x=60,y=298)
    lbl_txt10= Label(home, text='''     To Search On Github''', font=('Agency FB', 15),bg='white')
    lbl_txt10.place(x=7,y=330)
    lbl_txt11= Label(home, text=''' • Stk:''', font=('Agency FB', 18, 'bold'),bg='white')
    lbl_txt11.place(x=7,y=353)
    lbl_txt12= Label(home, text=''' <Your Query>''', font=('Agency FB', 18),bg='white')
    lbl_txt12.place(x=60,y=353)
    lbl_txt13= Label(home, text='''     To Search On StackOverFlow''', font=('Agency FB', 15),bg='white')
    lbl_txt13.place(x=7,y=385)

    try:
            socket.create_connection(('google.com',80))   
            b1 = Button(home, text="SEARCH", width=15, fg="PaleTurquoise", bg="Black", font=("Franklin Gothic Book",15,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=4 ,command=search_fn)
            b1.place(x=899, y=35)
    except OSError:
            b1 = Button(home, text="SEARCH", width=15, fg="PaleTurquoise", bg="Black", font=("Franklin Gothic Book",15,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=4 ,command=offline)
            b1.place(x=899, y=35)
        
    b2 = Button(home, text="↶", width=1, bg="white", fg="Black", font=("Arial",17), bd=1, overrelief=RIDGE, borderwidth=3, relief="solid", command=Back)
    b2.place(x=250, y=35)    
    b3 = Button(home, text="HISTORY", width=18, fg="Black", bg="PaleTurquoise", font=("Arial",15,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=2 ,command=ShowView)
    b3.place(x=6, y=527)
    b4 = Button(home, text="ABOUT", width=18, fg="Black", bg="PaleTurquoise", font=("Arial",15,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=2 ,command=About)
    b4.place(x=6, y=568)
    b5 = Button(home, text="EXIT", width=18, fg="Black", bg="PaleTurquoise", font=("Arial",15,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=2 ,command=Exit)
    b5.place(x=6, y=609)
    b6 = Button(home, text="↺", width=1, bg="white", fg="Black", font=("Arial",17), bd=1, overrelief=RIDGE, borderwidth=3, relief="solid", command=refresh)
    b6.place(x=1078, y=35)
    #--------------------------------------------------------------------------------------------------RANDOM PYTHON FACTS------------------------------------------------------------------------------------------------------

    lbl_txt = Label(home, text=" ------Random  Python Facts-------", font=('Agency FB', 15,'bold'),bg='white')
    lbl_txt.place(x=7,y=430)

    a = open('randinfo.txt','r')
    s=a.read()

    s=s.split('• ')
    i = len(s)-1
    index = randint(1,i)
    text =  s[index]
    text1 = scrolledtext.ScrolledText(home, height = 3, width = 22)
    text1.config(state="normal", font=("Times New Roman", "13"), borderwidth=4 , relief="solid")
    text1.insert(INSERT,text)
    text1.config(state='disabled')
    text1.place(x=6,y=460)

    a.close()

    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if SEARCH.get() !='':
        search_fn()

    else:
        pass

    home.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def  About():
    root = Toplevel()
    root.title('PyHelp Search Engine')
    root.resizable(0, 0)
    img = Image.open(path+"About.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def refresh():
    home.destroy()
    Home()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def history():
    
    val = SEARCH.get()
    val.lower()
    lt = ['lib','err','git','stk']
    v = val.split(':')
    if v[0] not in lt:
        v1 = 'None'
    else:
        v1 = v[0]
    try:
        v3 = v[1]
    except IndexError:
        v3 = v[0]
    v2 = str(datetime.date.today())

    database()#Calling database
    cursor.execute("INSERT INTO `history` (Type,Date,Query) VALUES(?, ?, ?)", (v1,v2,v3))
    conn.commit()

    cursor.close()
    conn.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def search_fn():
    history()
    speak('Processing. Please Wait')
    query = SEARCH.get()
    query.lower()
    
    
    if 'lib:' in query:

                tex = scrolledtext.ScrolledText(home, height = 8, width = 99)
                tex.config(state="normal", font=("Times New Roman", "13"), borderwidth=2 , relief="solid",bg='black',fg='white')
                a = query.split(':')
                

                def getData(url):
                    r = requests.get(url)
                    return r.text

                try:
                            x=a[1]
                except IndexError:
                            x=a[0]
                            x = x.split(' ')
                            x=x[1]

                myHtmlData = getData('https://pypi.org/project/'+x+"/#description")

                soup = BeautifulSoup(myHtmlData,'html.parser')
                lst=[]
                data = ''

                try:
                    for j in soup.find('span',id="pip-command"):
                        data = data + "PIP COMMAND: "
                        
                        data = data +str( j)
                        
                except TypeError:
                     data = 'Not Found !!!'
                     
                data = data + "\n"
                for clasg in soup.find_all('div', class_="project-description"):

                    p= clasg.find_all('p')

                    for i in p:

                        data = data + i.get_text()
                        data = data + "\n"

                if data=='Not Found !!!\n':
                    def getData(url):
                        r = requests.get(url)
                        return r.text

                    
                    data = ''
                    myHtmlData = getData("https://docs.python.org/3/py-modindex.html")


                    soup = BeautifulSoup(myHtmlData,'html.parser')


                    for clasg in soup.find_all('table', class_="indextable modindextable"):
                        d  =clasg.find_all('tr')
                        for i in d:
                            f = i.find_all('td')
                            
                            if x.lower() in str(f[1].get_text().lower()):
                                data = data + str(f[1].get_text())
                                data = data+"\n Description  ::        "+str(f[2].get_text())
                                
                                lnk="https://docs.python.org/3/"+f[1].find('a').get('href')
                                data = data+"\n Link ::     "+str(lnk)
                                data = data+"\n"
                                

                    if  data == '':
                        def opsite():
                            pass
                        def sp():
                            speak(data)
                            
                        b7b = Button(home, text="SPEAK", width=8, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=sp)
                        b7b.place(x=1036, y=282)            
                        b7a = Button(home, text="Nothing Found !!!", width=65, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=opsite)
                        b7a.place(x=236, y=282)

                        
                        tex.insert(INSERT,data)
                        tex.config(state='disabled')
                        tex.place(x=236,y=122)
                        
                    else:
                        def opsite():
                            webbrowser.open('https://docs.python.org/3/py-modindex.html')
                        def sp():
                            speak(data)
                            
                        b7b = Button(home, text="SPEAK", width=8, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=sp)
                        b7b.place(x=1036, y=282)
               
                        b7a = Button(home, text="OPEN THE OFFICIAL WEBSITE...", width=65, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=opsite)
                        b7a.place(x=236, y=282)
                        tex.insert(INSERT,data)
                        tex.config(state='disabled')
                        tex.place(x=236,y=122)
                else:
                        def opsite():
                            webbrowser.open('https://pypi.org/project/'+x+"/#description")
                        def sp():
                            speak(data)
                            
                        b7b = Button(home, text="SPEAK", width=8, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=sp)
                        b7b.place(x=1036, y=282)   
                        b7a = Button(home, text="OPEN THE OFFICIAL WEBSITE...", width=65, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=opsite)
                        b7a.place(x=236, y=282)
                        tex.insert(INSERT,data)
                        tex.config(state='disabled')
                        tex.place(x=236,y=122)

                lbl_ = Label(home, text=''' ---- MORE RELATED LINKS ----''', font=('Agency FB', 28),fg='white',bg='black',width=70)
                lbl_.place(x=236,y=329)
                text = scrolledtext.ScrolledText(home, height=14, width=99)
                text.config(state="normal", font=("Times New Roman", "13") , relief="solid",bg='black',fg='white')
                x=x+' python'
                def done():
                     links=[]
                     
                     for url in googlesearch.search(x, stop=20):
                          links.append(url)

                     def openb(lnk):
                          print (lnk['text'])
                          
                          webbrowser.open(lnk['text'])
                          
                     for i in range (len(links)):
                          t = links[i]
                               
                          button = Button(text, text=t,relief = FLAT,bg='black',fg='white')
                          button['command'] = lambda t = button: openb(t)
                          text.window_create(END, window=button)
                          text.insert(END,"\n")
                     text.config(state='disabled')
                     text.place(x=236,y=380)

                done()


    elif 'err:' in query:
        
                tex = scrolledtext.ScrolledText(home, height = 8, width = 99)
                
                tex.config(state="normal", font=("Times New Roman", "13"), borderwidth=2 , relief="solid",bg='black',fg='white')
                
                a = query.split(':')
                
                try:
                            x=a[1]
                except IndexError:
                            x=a[0]
                            x = x.split(' ')
                            x=x[1]
                            
                try:
                    d = wikipedia.summary(x, sentences=2)
        
                    def opsite():
                                webbrowser.open('https://en.wikipedia.org/wiki/'+x)
                    def sp():
                                speak(d)
                                
                    b7b = Button(home, text="SPEAK", width=8, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=sp)
                    b7b.place(x=1036, y=282)   
                    b7a = Button(home, text="OPEN THE OFFICIAL WEBSITE...", width=65, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=opsite)
                    b7a.place(x=236, y=282)                
                    tex.insert(INSERT,d)
                    tex.config(state='disabled')
                    tex.place(x=236,y=122)
                    
                except wikipedia.exceptions.PageError:
                    d = 'Nothing Found !!!'
        
                    def opsite():
                                pass
                    def sp():
                                speak(d)
                                
                    b7b = Button(home, text="SPEAK", width=8, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=sp)
                    b7b.place(x=1036, y=282)   
                    b7a = Button(home, text="Nothing Found On Wikipedia", width=65, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=6, relief="solid", command=opsite)
                    b7a.place(x=236, y=282)                
                    tex.insert(INSERT,d)
                    tex.config(state='disabled')
                    tex.place(x=236,y=122)                


                lbl_ = Label(home, text=''' ---- MORE RELATED LINKS ----''', font=('Agency FB', 28),fg='white',bg='black',width=70)
                lbl_.place(x=236,y=329)
                text = scrolledtext.ScrolledText(home, height=14, width=99)
                text.config(state="normal", font=("Times New Roman", "13") , relief="solid",bg='black',fg='white')
                x=x+' python'
                def done():
                     links=[]
                     
                     for url in googlesearch.search(x, stop=20):
                          links.append(url)

                     def openb(lnk):
                          print (lnk['text'])
                          
                          webbrowser.open(lnk['text'])
                          
                     for i in range (len(links)):
                          t = links[i]
                               
                          button = Button(text, text=t,relief = FLAT,bg='black',fg='white')
                          button['command'] = lambda t = button: openb(t)
                          text.window_create(END, window=button)
                          text.insert(END,"\n")
                     text.config(state='disabled')
                     text.place(x=236,y=380)

                done()

    elif 'git:' in query:
                a = query.split(':')
                
                try:
                            x=a[1]
                except IndexError:
                            x=a[0]
                            x = x.split(' ')
                            x=x[1]        

                def osite():
                                webbrowser.open('https://github.com/search?q='+x)
                    
                                

                b8a = Button(home, text="OPEN IN GITHUB...", width=75, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=5, relief="solid", command=osite)
                b8a.place(x=236, y=125)                
                

                                   


                lbl_ = Label(home, text=''' MORE RELATED LINKS ----''', font=('Agency FB', 28),fg='white',bg='black',width=70)
                lbl_.place(x=236,y=170)
                text = scrolledtext.ScrolledText(home, height=23, width=99)
                text.config(state="normal", font=("Times New Roman", "13") , relief="solid", borderwidth= 2,bg='black',fg='white')
                
                x=x+' python'
                def done():
                     links=[]
                     
                     for url in googlesearch.search(x, stop=20):
                          links.append(url)

                     def openb(lnk):
                          print (lnk['text'])
                          
                          webbrowser.open(lnk['text'])
                          
                     for i in range (len(links)):
                          t = links[i]
                               
                          button = Button(text, text=t,relief = FLAT,bg='black',fg='white')
                          button['command'] = lambda t = button: openb(t)
                          text.window_create(END, window=button)
                          text.insert(END,"\n")
                     text.config(state='disabled')
                     text.place(x=236,y=210)

                done()

    elif 'stk:' in query:
                a = query.split(':')
                
                try:
                            x=a[1]
                except IndexError:
                            x=a[0]
                            x = x.split(' ')
                            x=x[1]        

                def osite():
                                webbrowser.open('https://stackoverflow.com/search?q='+x)
                    
                                

                b8a = Button(home, text="OPEN IN STACKOVERFLOW...", width=75, bg="PaleTurquoise", fg="Black", font=("Arial",14,'bold'), bd=1, overrelief=RIDGE, borderwidth=5, relief="solid", command=osite)
                b8a.place(x=236, y=125)                
                

                                   


                lbl_ = Label(home, text=''' MORE RELATED LINKS ----''', font=('Agency FB', 28),fg='white',bg='black',width=70)
                lbl_.place(x=236,y=170)
                text = scrolledtext.ScrolledText(home, height=23, width=99)
                text.config(state="normal", font=("Times New Roman", "13") , relief="solid", borderwidth= 2,bg='black',fg='white')
                
                x=x+' python'
                def done():
                     links=[]
                     
                     for url in googlesearch.search(x, stop=20):
                          links.append(url)

                     def openb(lnk):
                          print (lnk['text'])
                          
                          webbrowser.open(lnk['text'])
                          
                     for i in range (len(links)):
                          t = links[i]
                               
                          button = Button(text, text=t,relief = FLAT,bg='black',fg='white')
                          button['command'] = lambda t = button: openb(t)
                          text.window_create(END, window=button)
                          text.insert(END,"\n")
                     text.config(state='disabled')
                     text.place(x=236,y=210)

                done()

    elif 'https' in query or 'www' in query:
        webbrowser.open(query)

    else:
                x = query
                text = scrolledtext.ScrolledText(home, height=27, width=99)
                text.config(state="normal", font=("Times heightNew Roman", "13") , relief="solid", borderwidth= 2,bg='black')
                
                
                def done():
                     links=[]
                     
                     for url in googlesearch.search(x, stop=20):
                          links.append(url)

                     def openb(lnk):
                          print (lnk['text'])
                          
                          webbrowser.open(lnk['text'])
                          
                     for i in range (len(links)):
                          t = links[i]
                               
                          button = Button(text, text=t,relief = FLAT,bg="black",fg='white')
                          button['command'] = lambda t = button: openb(t)
                          text.window_create(END, window=button)
                          text.insert(END,"\n")
                     text.config(state='disabled')
                     text.place(x=236,y=128)

                done()
    try:
        window.withdraw()
    except:
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ShowView():

    #Customising ViewForm

    global viewform
    viewform = Toplevel()
    viewform.title("History")
    width = 550
    height = 500
    
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

#=====================================================================================================

def ViewForm():

    #Creating A View Item Window

    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    

    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack()

    lbl_text = Label(TopViewForm, text="History", font=('impact', 24), width=600, bg="PaleTurquoise")
    lbl_text.pack(fill=X)
    
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    

    tree = ttk.Treeview(MidViewForm, columns=("S.No.", "Type", "Date", "Query"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('S.No.', text="S.No.",anchor=W)
    tree.heading('Type', text="Type",anchor=W)
    tree.heading('Date', text="Date",anchor=W)
    tree.heading('Query', text="Query",anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=110)
    tree.column('#3', stretch=NO, minwidth=0, width=120)

    tree.pack()
    showhist()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def showhist():

        database()

        cursor.execute("SELECT * FROM `history` ORDER BY s_no desc")
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor.close()
        conn.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Back():
    home.withdraw()
    window.state('normal')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def showhome():
    window.withdraw()
    Home()

    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def offline():
    time.sleep(1)
    speak('Oops... Internet Error!!! Check your internet and try again.')
    speak('Till then enjoy the game')
    os.startfile('dino.exe')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Show():
    vl= optionVar.get()
    if vl =='Day':
            a = datetime.date.today()
            a=str(a)
            speak(a)
            dayofweek = datetime.date.today().strftime("%A")
            speak(dayofweek)
            
    elif  vl =='Time':
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

    elif vl=='Calculator':
            import calculator
    elif vl=='Calendar':
        import cal

    elif vl =='Translator':
        import translator
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
window.title('PyHelp Search Engine')
window.resizable(0, 0)
img = Image.open(path+"cover.jpg")
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.pack(side="top", fill="both", expand="yes")


optionVar.set("---Widgets---")

# Create a option menu

option = OptionMenu(window, optionVar,'---Widgets---', "Time", "Day", "Calculator", "Calendar","Translator")
option.config(bg='PaleTurquoise', font=('arialnarrow', 15),borderwidth=4, relief = 'solid', width=61)
option.place(x=134,y=8)

btnShow = Button(window,fg='PaleTurquoise',bg='black', font=('arialnarrow', 13,'bold'),borderwidth=5, relief = 'solid', width=22, text="SHOW", command=Show)
btnShow.place(x=850,y=10)

search = Entry(window, textvariable=SEARCH, font=('arialnarrow', 30), width=32, bg="PaleTurquoise", borderwidth=6, relief = 'solid')
search.place(x=134,y=297)

 
try:
        socket.create_connection(('google.com',80))
        b = Button(window, text="SEARCH", width=15, fg="PaleTurquoise", bg="Black", font=("Franklin Gothic Book",18,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=4,command=showhome)
        b.place(x=850, y=297)
except OSError:
        
         b = Button(window, text="SEARCH", width=15, fg="PaleTurquoise", bg="Black", font=("Franklin Gothic Book",18,'bold'), relief="solid",bd=1, overrelief=RIDGE, borderwidth=4,command=offline)
         b.place(x=850, y=297)

         
speak('  welcome to Py Help Search Engine')       
window.mainloop()
