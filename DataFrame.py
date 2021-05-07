import pandas
df = pandas.read_csv('/home/user/Загрузки/titanic.csv')
#1
# print(df.columns)
#2
# people = len(df['Name'])
#3
# def mans():
#     a = 0
#     for x in df['Sex']:
#         if x == 'male':
#             a += 1
#     return a
# man = mans()
#
# def girls():
#     a = 0
#     for x in df['Sex']:
#         if x == 'female':
#             a += 1
#     return a
# girl = girls()
# #
# z = 0
# for i in df['Survived']:
#     if i == 1:
#         z += 1
#4
# print(z * 100 / people)
#5
# if girl > man:
#     print('Девушек было больше')
# else:
#     print('Пацанов было больше')
#6
# surv_mans = len(df[(df['Sex'] == 'male') & (df['Survived'] == 1)])
# print(surv_mans / z * 100)



                                #Task 38
info = pandas.read_csv('/home/user/Загрузки/info.csv')
marks = pandas.read_csv('/home/user/Загрузки/marks.csv')

x = marks.merge(info, left_on='id2', right_on='id')
# print(x.shape[0])
# print(info.shape[0] - x.shape[0])

group_a = x[x['race'] == 'group A']
group_a_sum = group_a['math'].sum()
average = group_a_sum / len(group_a)
# print(average)

y = marks.merge(info, left_on='id2', right_on='id', how='outer')
# print(y)

i = info.merge(marks, left_on='id', right_on='id2', how='left')
# print(i)

p = info.merge(marks, left_on='id', right_on='id2', how='right')
print(p)

