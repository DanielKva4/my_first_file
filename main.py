import re


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