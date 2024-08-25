class NLPapp:
    
    def __init__(self):
    
        self.__database = {}
        self.__first_menu() 
        
    def __first_menu(self):
        first_input = input("""
        Hello How would you like to procced
        1. Not a Member ? Register
        2. Already Member ? login
        3. Galti sa aa gaya ? Exit 
            """)
    
        
        if first_input =='1':
            self.__register()
        elif first_input =='2':
            self.__login()
        else:
            exit()
            
    def __second_menu(self):
        second_input = input("""
        Hello what NLP task you want to do 
        3. Named Entity Recogination
        4. language detection
        5. Sentiment analysis
        6. logout 
            """)
        if second_input =='3':
            self.__NER()
        elif second_input == '4':
            self.__language_detection()
        elif second_input =='5':
            self.__sentiment_analysis()
        elif second_input == '6':
            self.__logout()
        else:
            exit()
        
        
    def __register(self):
        name = input('enter your name')
        email = input('enter your email')
        password = input('enter your password')
        print('your info-->',self.__database)
        
    # check if user email  is existed in database  yes or not
        if email in self.__database:
            print('email already existed')
            # add the user is database if email is new 
        else:
            self.__database[email]= [name,password]
            print('login on it ')
        
    def __login(self):
        login_email = input('enter email')
        login_password = input('enter password ')
        
        if login_email in self.__database:
            # if email is correct then check password
            # convert into list --> it is 2d list 
            #db_values = list(self.__database.values())
            #if db_values[0][1] == login_password:
            if self.__database[login_email][1]== login_password:
                print('login succesful')
                self.__second_menu()
            else:
                print('Wrong passord try again ')
                self.__login()
            
        else:
            print('your email is not registere please first login')
            
    def __NER(self):
        pass
    def __language_detection(self):
        pass
    def __sentiment_analysis(self):
        pass
    def __logout(self):
        pass


sample_object = NLPapp()