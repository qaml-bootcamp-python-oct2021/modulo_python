import random

random_number = random.randint(1,20) * 2
print(random_number)
sum = 0

for num in range(1,99):
    if num == random_number:
        sum += num
        break
    sum += num

print(sum)