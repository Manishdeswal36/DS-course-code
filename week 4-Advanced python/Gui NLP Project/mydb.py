import json
# we import this class in gui app 
class DataBase:
    
    # for registration 
    def add_data(self,name,email,password):
        
        with open('db.json','r') as readfileobject:
            data_base = json.load(readfileobject)
            
        if email in data_base:
            return 0 # not register email already exist
        else:
            data_base[email]= [name,password]
            with open('db.json','w') as writefileobject:
                json.dump(data_base,writefileobject)
                
            return 1 # you are registed 
    
    # for login
    def search(self,email,password):
        
        with open('db.json','r') as read_file_object:
            data_base_dict = json.load(read_file_object)
            if email in data_base_dict:
                # in databse dict 2 item which is password math with password
                if data_base_dict[email][1]== password:
                    return 1
                else:
                    return 0
                
            else:
                return 0
                
