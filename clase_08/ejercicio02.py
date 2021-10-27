import random

my_list = []

index = 0

while index < 9:
    random_number = random.randint(1,9)
    print(f'Random number is {random_number}')  

   # print(my_list.count(random_number))
    if my_list.count(random_number) > 0:
        print(f'Number {random_number} already exists')  
        break
    else:
        my_list.append(random_number)
    index += 1
print(my_list)
    
