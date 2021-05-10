def Task_1(x):
    z = 0
    for y in x:
        z = z + y
    return z


# Task_1([1, 2, 3])


def Task_2(a):
    x = []
    for y in a:
        x.append(y / 2)
    return x


# print(Task_2([1, 2, 3, 4]))

def Task_3(a):
    x = 0
    for _ in a:
        x = x + 1
    return x
len()


# print(Task_3([1, 2, 3, 4, 8]))

def Task_4(a, b):
    for z in a:
        if z == b:
            return True
    return False


# print(Task_4([2,3,5],3))

def Task_5(a):
    x = 0
    suma = 0
    for _ in a:
        x += 1
    for i in a:
        suma += i
    return suma / x


# print(Task_5([2, 8, 6]))


def Task_6(ls):
    z = 0
    for x in ls:
        if x > z:
            z = x
    return z


# print(Task_6([3, 8, 6, 10]))

def Task_7(ls):
    mini = ls[0]
    for x in ls:
        if x < mini:
            mini = x
    return mini


# print(Task_7 ([6, 3, 8 , 6, 10]))


def Task_8(a):
    for x in a:
        if x % 2 == 0:
            print(x)
    return


# Task_8([3,7,4,8])


def Task_9(a):
    for x in a:
        if x % 2 > 0:
            print(x)
    return


# Task_9([3,7,4,8])


def Task_10(a, b):
    x = []
    for i in a:
        if i in b:
            x.append(i)
    return print(x)


# Task_9([3,7,4,8], [7, 5, 3, 4])


def Task_11(a, b):
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    return print(x)


# Task_11([3, 5, 7], [3, 5, 6])

def Task_11_2(a, b):
    x = 0
    for i in range(b):
        x = x + a
    return print(x)


# Task_11_2(2, 15)

def Task_12(x, y):
    i = 1
    for q in range(y):
        i *= x
    return print(i)


# Task_12(3, 2)

def Task_13():
    for i in range(1, 11):
        print(str(i) + ' * ' + str(i) + " = " + str(i * i))
    return


# Task_13()

def Task_14(a):
    print(' ' * 3 + str(a[0]))
    y = len(str(a[0]))
    for i in a[1:]:
        z = len(str(i))
        q = 3 + y - z
        print(' ' * q + str(i))


# Task_14([13, 2, 333])


def Task_15():
    people = 0
    while True:

        x = input('1 число: ')
        y = input('2 число: ')
        z = input('Ответ : ')
        if x <= str(0) or y <= str(0) or z <= str(0):
            print('You lose')
            break
        if int(z) == int(x) * int(y):
            people += 1
        if int(z) != int(x) * int(y):
            print('Miss')
            people -= 1
        print('У тебя ' + str(people) + ' очко(в)')


# Task_15()

def Task_16(a):
    z = 0
    q = 0
    for x in a:
        if x > z:
            z = x
    for u in a:
        if q < u < z:
            q = u
    print([z, q])
    return


# Task_16([1, 2, 3, 4, 5])

def Task_17():
    a = list(range(4))
    for x in a:
        print('****')
    return


# Task_17()

def Task_18(a):
    z = a - 2
    print('*' * a)
    for x in range(z):
        print('*' + ' ' * z + '*')
    print('*' * a)


# Task_18(8)

def Task_19(a):
    z = a - 2
    for x in range(z):
        print('*' * a)
        print(' ' + '*' * a)
    return


# Task_19(4)

def Task_20(a, b):
    x = range(a, b)
    for i in x:
        if i % 2 == 0:
            print(i)
    return


# Task_20(3, 15)

def Task_21(a):
    x = 1
    for y in range(1, a + 1):
        x = x * y
    return x


# print(Task_21(5))

def Task_22(a, b, c):
    for x in range(c):
        z = a / 100 * b
        a += z
    return a


# print(Task_22(40, 50, 3))

def Task_23(a):
    if a % 2 == 0:
        return False
    else:
        return True


# print(Task_23(11))

def Task_24(a):
    for x in range(1, a + 1):
        print('*' * x)
    return

# Task_24(5)

def Task_25(a):
    space = ' '
    gaps = a
    for x in range(1, a + 1, 2):
        print(space * gaps + '*' * x)
        gaps -= 1
    gaps += 2
    for z in range(a - 2, 0, -2):
        print(space * gaps + '*' * z)
        gaps += 1

# Task_25(19)


                        # WITH WHILE





