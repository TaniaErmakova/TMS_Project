class Auto:
    weight = 1

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')


    def stop(self):
        print('stop')


    def birthday(self):
        self.age +=1  #изменение атрибута класса с помощью метода
        print(self.age)


