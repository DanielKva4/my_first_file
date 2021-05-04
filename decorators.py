import math

def my_decor(fn):
    def work(a):
        x = fn(a)
        return x.capitalize()
    return work



@my_decor
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]
# print(swap_words('дал коля'))


def dec2(fn):
    def workaem(a):
        x = fn(a)
        return fn(x)
    return workaem

@dec2
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result
# print(mult_on_2([1, 2, 3, 4]))


def decor3(fn):
    def work_ok(a):
        try:
            x = fn(a)
        except Exception as e:
            print('Я не принимаю отрицательные числа')
            return -1
        return x
    return work_ok

@decor3
def my_sqrt(x):
    return math.sqrt(x)
print(my_sqrt(-4))