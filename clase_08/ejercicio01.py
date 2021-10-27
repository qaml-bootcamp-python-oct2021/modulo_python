import random

random_number = random.randint(1,10)
my_list = [1,2,3,4,5]



def list_len():
    return len(my_list)

def validate_random():
    if my_list.count(random_number) > 1:
        index = 0
        while index < list_len():
            if random_number == my_list[index]:
                my_list.pop(index)
                break
            index += 1
    else: 
        my_list.pop(0)


print(f'List is {list_len()} items length')  
print(f'Random number is {random_number}')  
my_list.append(random_number)
validate_random()
print(f'New list is {my_list} items length')  
print(f'List is {list_len()} items length')  
