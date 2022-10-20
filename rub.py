def out(number):
    num = str(number)    
    result = list(num)  #Список цифр
    len_check = len(result)
    output = [] 
    if len(result) > 6:
        print('Число не входит в диапозон')
    #Дополняем список нулями до 6 цифр
    while len(result) < 6:
        zero = ['0']
        result = zero + result
    #Проверяем цифру из списка, ставим строку в соответствие   
    if result[0] != '0':
        if result[0] == '1': a0 = 'сто'
        if result[0] == '2': a0 = 'двести'
        if result[0] == '3': a0 = 'триста'
        if result[0] == '4': a0 = 'четыреста'
        if result[0] == '5': a0 = 'пятьсот'
        if result[0] == '6': a0 = 'шестьсот'
        if result[0] == '7': a0 = 'семьсот'
        if result[0] == '8': a0 = 'восемьсот'
        if result[0] == '9': a0 = 'девятьсот'
        output.append(a0)
    if result[1] != '0':
        if result[1] == '2': a1 = 'двадцать'
        if result[1] == '3': a1 = 'тридцать'
        if result[1] == '4': a1 = 'сорок'
        if result[1] == '5': a1 = 'пятьдесят'
        if result[1] == '6': a1 = 'шестьдесят'
        if result[1] == '7': a1 = 'семьдесят'
        if result[1] == '8': a1 = 'восемьдесят'
        if result[1] == '9': a1 = 'девяносто'
        if result[1] == '1':
            if result[2] == '0': a1 = 'десять'
            if result[2] == '1': a1 = 'одиннадцать'
            if result[2] == '2': a1 = 'двенадцать'
            if result[2] == '3': a1 = 'тридцать'
            if result[2] == '4': a1 = 'четырнадцать'
            if result[2] == '5': a1 = 'пятнадцать'
            if result[2] == '4': a1 = 'шестьнадцать'
            if result[2] == '7': a1 = 'семнадцать'
            if result[2] == '8': a1 = 'восемнадцать'
            if result[2] == '9': a1 = 'девятнадцать'
        output.append(a1)
    if result[2] != '0':
        if result[1] != '1':
            if result[2] == '1': a2 = 'одна'
            if result[2] == '2': a2 = 'две'
            if result[2] == '3': a2 = 'три'
            if result[2] == '4': a2 = 'четыре'
            if result[2] == '5': a2 = 'пять'
            if result[2] == '6': a2 = 'шесть'
            if result[2] == '7': a2 = 'семь'
            if result[2] == '8': a2 = 'восемь'
            if result[2] == '9': a2 = 'девять'
            output.append(a2)
    if len_check > 3:
        output.append('тысяч')
    #Подбираем падеж
    if result[2] != '0':
        if result[1] != '1':
            if result[2] == '1':
                output.pop()
                output.append('тысяча') 
            if result[2] == '2':
                output.pop()
                output.append('тысячи')
            if result[2] == '3':
                output.pop()
                output.append('тысячи')
            if result[2] == '4':
                output.pop()
                output.append('тысячи')
    if result[3] != '0':
        if result[3] == '1': a3 = 'сто'
        if result[3] == '2': a3 = 'двести'
        if result[3] == '3': a3 = 'триста'
        if result[3] == '4': a3 = 'четыреста'
        if result[3] == '5': a3 = 'пятьсот'
        if result[3] == '6': a3 = 'шестьсот'
        if result[3] == '7': a3 = 'семьсот'
        if result[3] == '8': a3 = 'восемьсот'
        if result[3] == '9': a3 = 'девятьсот'
        output.append(a3)
    if result[4] != '0':
        if result[4] == '2': a4 = 'двадцать'
        if result[4] == '3': a4 = 'тридцать'
        if result[4] == '4': a4 = 'сорок'
        if result[4] == '5': a4 = 'пятьдесят'
        if result[4] == '6': a4 = 'шестьдесят'
        if result[4] == '7': a4 = 'семьдесят'
        if result[4] == '8': a4 = 'восемьдесят'
        if result[4] == '9': a4 = 'девянсто'
        if result[4] == '1':
            if result[5] == '0': a4 = 'десять'
            if result[5] == '1': a4 = 'одиннадцать'
            if result[5] == '2': a4 = 'двенадцать'
            if result[5] == '3': a4 = 'тринадцать'
            if result[5] == '4': a4 = 'четырнадцать'
            if result[5] == '5': a4 = 'пятнадцать'
            if result[5] == '6': a4 = 'шестнадцатьь'
            if result[5] == '7': a4 = 'семнадцать'
            if result[5] == '8': a4 = 'восемнадцать'
            if result[5] == '9': a4 = 'девятнадцать'
        output.append(a4)
    if result[5] != '0':
        if result[4] != '1':
            if result[5] == '1': a5 = 'один'
            if result[5] == '2': a5 = 'два'
            if result[5] == '3': a5 = 'три'
            if result[5] == '4': a5 = 'четыре'
            if result[5] == '5': a5 = 'пять'
            if result[5] == '6': a5 = 'шесть'
            if result[5] == '7': a5 = 'семь'
            if result[5] == '8': a5 = 'восемь'
            if result[5] == '9': a5 = 'девять'
            output.append(a5)
    #Подбираем падеж
    output.append('рублей')
    if result[5] != '0':
        if result[4] != '1':
            if result[5] == '1':
                output.pop()
                output.append('рубль') 
            if result[5] == '2':
                output.pop()
                output.append('рубля')
            if result[5] == '3':
                output.pop()
                output.append('рубля')
            if result[5] == '4':
                output.pop()
                output.append('рубля')
    print(str.capitalize(' '.join(output)))
