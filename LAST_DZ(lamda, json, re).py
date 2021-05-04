y = list(map(lambda x: x + 100, [4,5,6]))
# # print(y)

z = list(filter(lambda x: , [4,5,6]))
# print(z)


import statistics
y = [1, 2, 3, 4, 5]
statistics.mean(y)
#
from statistics import mean
mean(y)

import math
# math.factorial(5)

from math import factorial
factorial(5)

import json
x = json.dumps([1, 2, 3, 4])

from json import dumps
dumps([1, 2, 3])

from json import loads
zz = (loads(x))
# # print(zz[0])
#
from django.http import HttpResponse
#
#
import re
#
# print(re.match('^\s$', ' ') is not None)
#
# print(re.match('^\d$', '2') is not None)
#
# print(re.match('^\d\d$', '22') is not None)
#
# print(re.match('^\s\s\s$', '   ') is not None)
#
# print(re.match('^a\dv$', 'a7v') is not None)

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

