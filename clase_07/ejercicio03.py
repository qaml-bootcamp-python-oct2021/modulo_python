import random
random_number = random.randint(0,10)

my_value = input("Type a number:")
number_try = 1


while random_number != int(my_value):
    print(f'Try number {number_try} with random number {random_number}')  
    #print(my_value)
    #print(random_number)
    number_try += 1
    random_number = random.randint(0,10)

print(f'It took {number_try} tries to have a match with {random_number}')  

