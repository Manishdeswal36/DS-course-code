class Scoop:
    def __init__(self,flavor,price) -> None:
        self.flavor = flavor
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if type(new_price) == int:
            self.__price = new_price
            return 'the new price is',self.__price
        else:
            return 'please enter valid price int-datatype'
    
    def __str__(self) -> str:
        return 'flavor - {}, price - {}'.format(self.flavor,self.__price)
        
class Bowl(Scoop):
    # it handle multiple parameters according to need we use args
    def __init__(self) -> list:
        super()
        self.__scoop_list = []
        
    def add_scoop(self,*new_scoops):
        for i in new_scoops:
            self.__scoop_list.append(i)
        return self.__scoop_list
    def display(self):
        total = 0
        for i in self.__scoop_list:
            total = 0
            print(i)


scoop_object_1 = Scoop('chocolate',20)
scoop_object_2 = Scoop('vanilla',30)
scoop_object_3 = Scoop('banana',40)
bowl_object_1 = Bowl()#
bowl_object_1.add_scoop(scoop_object_1,scoop_object_2,scoop_object_3)

print(bowl_object_1.add_scoop())
print(bowl_object_1.display())
