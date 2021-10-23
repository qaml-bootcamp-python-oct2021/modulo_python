total = 0
def sumatoria(num):
    while num >= total:
        suma = num + total
        num -=1
    return suma

print(sumatoria(5))