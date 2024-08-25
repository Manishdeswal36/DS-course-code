# make a dictionary of pair of number now choice from the random
# only dict keys then ask the user the print the dictinary value
# check if dict key = dict value  increase the point otherwise 0 
import random
pair_of_num= {
    1:10,
    2:20,
    3:30,
    4:40,
    5:50
}
pair_of_num.keys()
type(pair_of_num.keys())
random_key_num = random.choice(list(pair_of_num.keys()))
# oo it takes only sequence data type not mapping
print('the random key num is :',random_key_num)
user_value_num = int(input('enter the dict value:  '))

if user_value_num == pair_of_num.values():
    print('your dict value is {} which match in dict'.format(user_value_num))
else:
        print('your dict value is {} which NOT match in dict'.format(user_value_num))

