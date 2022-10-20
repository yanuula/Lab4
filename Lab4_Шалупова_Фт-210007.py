import rub #Импортирвоание кода для вывода суммы в рублях, которую необходимо заплатить за просчитанный вариант (цифрами)
while True:
    try:
        employees_num = int(input('Введите число сотрудников: ')) #Ввод числа сотрудников 
        assert 1 <= employees_num <= 1000
    except AssertionError:
        print('Число не входит в диапазон')
        break
    except ValueError:
        print('Введите число')
        break
    sum = 0
    distance_list = []
    price_list = []
    try:
        distance_list = list(map(int, input("Введите расстояние в километрах, используя пробел: ").split())) #Ввод расстояния 
        price_list = list(map(int, input("Введите тарифы за проезд одного километра, используя пробел: ").split())) #Ввод тарифов 
    except ValueError:
        print('Неверный ввод')
        break
    c_distance_list = distance_list[:] #Копии списков
    c_price_list = price_list[:]
    index_list_d = [] #Списки с индексами значений 
    index_list_p = []
    #Заполнение списков индексами 
    max_distance = 0
    for i in range(employees_num):                              
        index = c_distance_list.index(max(c_distance_list))
        index_list_d.append(index)
        c_distance_list[index] = 0
    for i in range(employees_num):
        index = c_price_list.index(min(c_price_list))
        index_list_p.append(index)
        c_price_list[index] = 10**10
    print('Такси для клиентов по порядку: ') #Вывод такси для клиентов 
    for i in range(employees_num):
        taxi_num = index_list_p[index_list_d.index(i)]
        print(taxi_num+1)
    for i in range(employees_num):
        sum += distance_list[index_list_d[i]]*price_list[index_list_p[i]]
    print('Сумма: ')
    print(sum) #Вывод суммы
    rub.out(sum) 
