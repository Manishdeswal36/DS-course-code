# n = int(input('enter the number'))
# binary = []
# while n > 0:
#     binary.append(n%2) # divide and store the remainder 
#     n = n//2  # every time divide the next decrement term 
#     print(n, binary)

# print(binary)
# x = int(input('enter your 1st number: '))
# y = int(input('enter your 2nd number: '))
# if x > y:
#     gretor = x
# else: 
#     gretor = y 

# while True:
#     if (gretor % x == 0 )  and (gretor % y == 0 ) :
#         lcm = gretor
#         break
#     gretor = gretor+1

# print(lcm)
x = int(input('enter your 1st number: '))
y = int(input('enter your 2nd number: '))
if y > x:
    smaller = x
else: 
    smaller = y 

for i in range(1, smaller+1):
    if (x % i == 0 )  and (y % i == 0 ) :
        hcf = i 

print(hcf)
