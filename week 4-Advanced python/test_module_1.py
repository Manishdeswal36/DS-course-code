def Namaskar():
    print('namaskar shrishti')
    
# # call the func
# Namaskar()
# print(__name__)

from mymath.trignometry.sin import mysin

print(mysin(45))


def square(num):
    print(num**2)
    
def main():
    for i in range(1,11):
        square(i)
    
if __name__== '__main__':
    pass
    #main()
    
# for i in range(1,11):
#     square(i)

# if __name__ == 'main':
#     for i in range(1,11):
#         square(i)
# agar file ka name __main_ ha tho tabhi iss code ko execute karna

