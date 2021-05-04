class Human:
    def __init__(self, age, color, eaten_candy):
        self.age = age
        self.color = color
        self.candy = eaten_candy

    def eating(self, konfeta):
        self.candy.append(konfeta)

danila = Human(20, 'white', [])
danila.eating('nutella')
danila.eating('alenka')
# print(danila.candy)


class Dress:
    def __init__(self, sort, color, rost):
        self.sort = sort
        self.color = color
        self.rost = rost

    def delaem_rost(self, rost_dreva):
        self.rost = self.rost + rost_dreva

brevno = Dress('dub', 'green', 100)

brevno.delaem_rost(5)
# print(brevno.rost)



class Home:
    def __init__(self, coast, rooms):
        self.coast = coast
        self.rooms = rooms
my_house = Home(35000, 3)
# print(my_house.coast)

class Book:
    def __init__(self, pages, autor):
        self.pages = pages
        self.autor = autor

    def printing(self, printim):
       print(self.pages[printim])


Harry_Potter = Book(['privet', 'kak dela', 'nikak?', 'poka'], 'Angelina')
# Harry_Potter.printing(0)

# print(Harry_Potter.__dict__)

class Time:
    def __init__(self, year, mounth, day):
        self.year = year
        self.mounth = mounth
        self.day = day


a24_05_2021 = Time(2021, 'April', 24)
# print(a24_05_2021.__dict__)

class Mail:
    def __init__(self, massage, info):
        self.massage = massage
        self.info = info
    def p_s(self, ps):
        self.massage += ps

pismo = Mail('Ты годен', 'Минск, Тимирязева 67, каб. 816')
pismo.p_s('\n\nC уважением, военкомат')
print(pismo.massage)