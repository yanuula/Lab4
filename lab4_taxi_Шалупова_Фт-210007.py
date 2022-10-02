def BubbleSort(A):
    j = len(A) - 1
    flag = True
    while flag: 
        flag = False
        for i in range (0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                flag = True
        j -= 1
 
 
n = int(input("Введите количество сотрудников в компании: ")) 
people = list(map(int, input("Введите расстояние в километрах, используя пробел: ").split())) 
taxi = list(map(int, input("Введите тарифы за проезд одного километра, используя пробел: ").split())) 
for i in range(n):
    people [i] = (people [i], i + 1)
for i in range (n):
    taxi[i] = (-taxi[i], i + 1) 
BubbleSort(people) 
BubbleSort(taxi) 
ans = [0] * (n + 1) 
for i in range(n): 
    ans[people[i][1]] = taxi[i][1] 
for i in range(1, n + 1): 
    print(ans[i], end=' ')
