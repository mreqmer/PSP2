from random import randint
from threading import *
from time import sleep


class Mesa(Thread):
    palillos = [False] * 5
    cond = Condition()
    def __init__(self):
        Thread.__init__(self)


class Filosofo(Thread):
    def __init__(self, nombre, numero):
        Thread.__init__(self, name= nombre)
        self.numero = numero

    def run(self):
        while(True):
            print("Filosofo " + self.name +" está pensando")
            sleep(randint(1,3))
            with Mesa.cond:
                while Mesa.palillos[self.numero]: # está cogido
                    print("Filosofo " + self.name +" Esperando por palillos a la izquierda")
                    Mesa.cond.wait()
                while Mesa.palillos[(self.numero + 1) % 5]:
                    print("Filosofo " + self.name +" Esperando por palillos a la derecha")
                    Mesa.cond.wait()

            Mesa.palillos[self.numero] = True
            Mesa.palillos[(self.numero + 1) % 5] = True

            print("Filosofo " + self.name + " comiendo")
            sleep(randint(1,9))

            with Mesa.cond:
                Mesa.palillos[self.numero] = False
                Mesa.palillos[(self.numero + 1) % 5] = False
                print(f"Filósofo {self.name} ha terminado de comer y libera los palillos.")
                Mesa.cond.notify_all()



if __name__ == '__main__':

    m = Mesa()

    for i in range(5):
        f = Filosofo(f"F{i}", i)
        f.start()






