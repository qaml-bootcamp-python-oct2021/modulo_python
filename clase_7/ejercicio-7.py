def multiplos_de_tres():
    res = ''
    for number in range(0,100,2):
        if(number % 3 == 0): continue
        res += '{},'.format(number)
    print(res)
multiplos_de_tres()