import re

# print(re.match("^[HBMP][HBMP]\d{7}$", 'PB1234567') is not None)

# print(re.match('^(Привет|Добрый день|Салют)\sдорогой юзер$', 'Привет дорогой юзер') is not None)

# print(re.match('^\d\s(\+|\/|\*)\s\d$', '5 * 5') is not None)

# print(re.match('^a\d+c$', 'a777c') is not None)

def login():
    x = input('get_login: ')
    if re.match('^.+@gmail\.com$', x) is None:
        raise Exception("Ты лох")
    else:
        return re.match('^(.+)@gmail\.com$', x).groups()


# print(login())

def regai():
    x = '<a>privet<a>'
    if re.match('^<.+>.+<.+>$', x) is not None:
        return re.match('^<.+>(.+)<.+>$', x).groups()
    else:
        raise Exception('Условие функции глянь дурень')

# print(regai())

def fn_5(x):
    if re.match('^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}$', x) is not None:
        x = re.match('^\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2}):\d{2}$', x).groups()
        return x
    else:
        raise Exception("Нипанятна")
print(fn_5('2018-01-09 12:32:01'))



def fn_6():
    x = input('ебош дискриминант: ')
    if re.match('^-?\d+\.?\d*\s[\+\*-/]\s-?\d+\.?\d*$', x) is not None:
        y = float(re.match('^(-?\d+\.?\d*)\s[\+\*-/]\s-?\d+\.?\d*$', x).groups()[0])
        z = float(re.match('^-?\d+\.?\d*\s[\+\*-/]\s(-?\d+\.?\d*)$', x).groups()[0])
        u = re.match('^-?\d+\.?\d*\s([\+\*-/])\s-?\d+\.?\d*$', x).groups()[0]
        sl = {'*': y * z, '+': y + z, '-': y - z, '/': y / z}
        return sl[u]
    else:
        raise Exception('asds')

# print(fn_6())