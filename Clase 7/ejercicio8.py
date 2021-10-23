import random

num = random.randint(1, 20) * 2
num2= 0

print(num)

for ciclo in range(1,99,1):
   num2 += ciclo 
   if ciclo == num:
    break 

print(num2)