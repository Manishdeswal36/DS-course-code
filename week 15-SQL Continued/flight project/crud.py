import mysql.connector

try :
    connector_object = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'improve@7',
        database = 'indigo'
    )
    mycursor = connector_object.cursor()
    print('Connection established')
except:
    print('Connection Error')
    
# create a database in the server 
# mycursor.execute('CREATE DATABASE indigo')
# connector_object.commit()

# create a table 
# name of airport airporot id | code |name |city
# mycursor.execute('''
#     CREATE TABLE airport(
#         airport_id INTEGER PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         city VARCHAR(50) NOT NULL,
#         name VARCHAR(255) NOT NULL
#     )
#                 ''')

# connector_object.commit()

# now we perform the crud operations in the table 
# cread ,retrive,update ,delelte 
# now add some airports data 

# Insert the data
# mycursor.execute('''
#     INSERT INTO  airport values
#     (1,'DEL','New Delhi','IGIA'),
#     (2 ,'CCU', 'kolkata','NSCA'),
#     (3 ,'BOM', 'Mumbai','CSMA')
#                 ''')
# connector_object.commit()

# retreive the data 

    
# now aap tkinder use kareka data ko app ma display karo 
# flask use kareka website ma display karo data ko
# ya fastapi use karka kisi api ma 
# ya streamlit use karka ksi website par 

# update example 
# mycursor.execute('''
#             UPDATE airport
#             SET name = 'Bombay'
#             WHERE airport_id = 3
#                 ''')
# connector_object.commit()


    
# delelte the bombay airport 
mycursor.execute('''
            DELETE FROM airport WHERE airport_id = 3
                ''')

# now retrive the data 
mycursor.execute('SELECT * FROM airport ')
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])