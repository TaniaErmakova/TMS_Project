import time
class Auto:

    def move(self):
        print('move')


class Truck(Auto):

    def __init__(self, max_load):
        self.max_load = max_load

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

    def move(self):
        super().move()
        print("attention")


class Car(Auto):

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        print('move')
        print("max_speed is <max_speed>")


Volvo = Truck(2)
Volvo.move()
Volvo.load()

MAN = Truck(3)
MAN.move()
MAN.load()

KIA = Car(200)
KIA.move()

Ferrari = Car(300)
Ferrari.move()