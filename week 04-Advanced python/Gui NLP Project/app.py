from tkinter import *
from mydb import DataBase
from tkinter import messagebox
from myapi import API

class NLPApp:
    
    def __init__(self) -> None:
        # create a object of database class
        self.dbobject = DataBase()
        self.apiobject = API()
        # login ka gui code load hoga
        self.root = Tk()
        self.root.title('NLp App')
        self.root.iconbitmap(r'resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.config(background='#5d6d7e')
        #self.login_gui()
        self.home_gui()
        self.root.mainloop() 
        
    def login_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLP App',background='#5d6d7e',foreground='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label_1 = Label(self.root,text='Enter Email')
        label_1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=7)
        
        label_2 = Label(self.root,text='Enter password')
        label_2.pack(pady=(10,10))
        
        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=7)
        
        login_button = Button(self.root,text='login',width=30,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))
        
        label_3 = Label(self.root,text='Not a member')
        label_3.pack(pady=(10,10))
        
        redirect_button = Button(self.root,text='Register Now',width=15,height=1,command=self.register_gui)
        redirect_button.pack(pady=(10,10))
        
    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLP App',background='#5d6d7e',foreground='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label_0 = Label(self.root,text='Enter Name')
        label_0.pack(pady=(10,10))
        
        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=7)
        
        label_1 = Label(self.root,text='Enter Email')
        label_1.pack(pady=(10,10))
        
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=7)
        
        label_2 = Label(self.root,text='Enter password')
        label_2.pack(pady=(10,10))
        
        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=7)
        
        register_button = Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_button.pack(pady=(10,10))
        
        label_3 = Label(self.root,text=' Already amember')
        label_3.pack(pady=(10,10))
        
        redirect_button = Button(self.root,text='login',width=15,height=1,command=self.login_gui)
        redirect_button.pack(pady=(10,10))
        
    def clear(self):
        # clear the existing gui 
        for i in self.root.pack_slaves():
            i.destroy()
            
    def perform_registration(self):
        # fetch data from gui 
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbobject.add_data(
            name=name, # input object = database object 
            email= email,
            password=password
            )
        if response:
            messagebox.showinfo(title='sucess',message='registration succesfully.you can login now ')
        else:
            messagebox.showerror(title='Error',message='Email already existed ')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        # input email = database email 
        response = self.dbobject.search(email=email, password= password)
        
        if response:
            messagebox.showinfo('success','login sucessfully')
            self.home_gui()
        else:
            messagebox.showerror('error',"your email and password is incorrect")
            
    def home_gui(self):
        self.clear()
        
        heading = Label(self.root,text='NLP App',background='#5d6d7e',foreground='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        sentiment_button = Button(self.root,text='Sentiment Analysis ',width=30,height=4,command=self.sentiment_gui)
        sentiment_button.pack(pady=(15,15))
        
        ner_button = Button(self.root,text='Named Entity Recognitation ',width=30,height=4,command=self.ner_gui)
        ner_button.pack(pady=(15,15))
        
        emotion_button = Button(self.root,text='Emotion Predection',width=30,height=4,command=self.emotion_gui)
        emotion_button.pack(pady=(15,15))
        
        logout_button = Button(self.root,text='logout ',width=10,height=1,command=self.login_gui)
        logout_button.pack(pady=(15,10))
        
    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#5d6d7e', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#5d6d7e', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label_1 = Label(self.root, text='Enter the text')
        label_1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=10)

        sentiment_button = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='show result',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        go_back_button = Button(self.root, text='Go back',command=self.home_gui )
        go_back_button.pack(pady=(10, 10))
        
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apiobject.sentiment_analysis(text=text)
        print(result)
        
    def ner_gui(self):
        self.clear()
        
    def emotion_gui(self):
        self.clear()
        
nlp = NLPApp()