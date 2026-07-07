for num in range(1000,10000):
    number = str(num)
    reverse_flash = number[3] + number[2] + number[1] + number[0] 
    if (num * 4) == int(reverse_flash):
        print(num)