import mysql.connector

class DB:
    def __init__(self):
        # connect to the database 
        try :
            self.connector_object = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'improve@7',
                database = 'campusx'
            )
            self.mycursor = self.connector_object.cursor()
            print('Connection established')
        except:
            print('Connection Error')
            
            
    def fetch_city_names(self):
        self.mycursor.execute('''
                            
        SELECT DISTINCT(Source) FROM flights
        UNION
        SELECT DISTINCT(Destination) FROM flights
                            ''')
        
        data = self.mycursor.fetchall()
        city = []
        for item in data:
            city.append(item[0])
            
        return city
    
    
    def fetch_all_flights(self,input_source, input_destination):
        
        self.mycursor.execute(f'''
                            SELECT Airline,Route,Dep_Time , price FROM flights
                            WHERE Source = '{input_source}' AND Destination = '{input_destination}'
                            ''')
        
        data = self.mycursor.fetchall()
        
        return data
        
    
    def fetch_airline_frequency (self):
        
        self.mycursor.execute('''
                            SELECT Airline, COUNT(*)  AS num_of_flights
                            from flights
                            GROUP BY Airline
                            ORDER BY num_of_flights DESC
                            ''')
        
        data = self.mycursor.fetchall()
        
        airline = []
        for item in data:
            airline.append(item[0])
        
        frequency = []
        for item in data:
            frequency.append(item[1])
            
        return airline,frequency
    
    def busy_airport(self):
        
        self.mycursor.execute('''
                            SELECT Source,COUNT(*) FROM (SELECT Source FROM flights
							UNION ALL
							SELECT Destination FROM flights) t
                            GROUP BY t.Source
                            ORDER BY COUNT(*) DESC
        ''')
        
        data = self.mycursor.fetchall()
        
        cities = []
        for item in data:
            cities.append(item[0])
        
        frequency = []
        for item in data:
            frequency.append(item[1])
            
        return cities,frequency
    
    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flights
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency