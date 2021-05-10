from re import match

#Составьте программу, выводящую на экран квадраты чисел от 10 до 20 включительно
def Task_1():
    for i in range(10, 21):
        print(i * i)
    return
# Task_1()

#Даны натуральные числа от 35 до 87. Вывести на консоль те из них, которые при делении на 7 дают остаток 1, 2 или 5
def Task_2():
    for i in range(35, 88):
        if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:
            print(i)
    return
# Task_2()

def Task_3():
    x = int(input('Введи число: '))
    z = 0
    for i in range(1, x + 1):
        z += i
    return z
# print(Task_3())


def Task_4(q):
    if match('^\d{3}$', q) is not None:
        a = int(q[0])
        b = int(q[1])
        c = int(q[2])
        return a + b + c
    else:
        raise Exception('3 циферки должно быть')
# print(Task_4('123'))

def Task_5(a):
    z = 0
    for i in range(1, a + 1):
        if i % 2 == 0:
            z += 1
    return z
# print(Task_5(6))



def Task_6(a):
    z = []
    for i in str(a):
        z.append(int(i))
    return max(z)
# print(Task_6(123))

def Task_7():
    q = []
    for i in range(1000, 10000):
        z = list(map(int, str(i)))
        if sum(z) == 15:
            q.append(i)
    return q
# print(Task_7())

def Task_8():
    n = int(input("Введите число: "))
    i = 2
    while n > i:
        if n % i != 0:
            i += 1
        else:
            return print("Число не простое")
    return print('Число простое')
# Task_8()

def Task_8_1():
    x = int(input('Число: '))
    for z in range(2, x + 1):
        if x % z != 0:
            continue
        elif x == z:
            return print('Число простое')
        else:
            return print("Число не простое")
    return print('Число простое')
# Task_8_1()

def Task_9():
    x = int(input('Число: '))
    z = []
    for i in range(x, 0, -1):
        if x % i == 0:
            z.append(i)
    return z
print(Task_9())

