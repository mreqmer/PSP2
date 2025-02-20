from random import randint
from threading import *
from time import sleep


class EscapeRoom:
    codigo_secreto = 1
    barrera = Barrier(5)

class Jugador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.codigo = 0

    def run(self):
        print(f"Jugador {self.name} está intentando adivinar la clave")

        while self.codigo != EscapeRoom.codigo_secreto:
            sleep(randint(1,3))
            self.codigo = randint(1,10)

        print(f"Jugador {self.name} adivinó la clave {self.codigo}")

        EscapeRoom.barrera.wait()

        print(f"Jugador {self.name} ha salido.")

if __name__ == "__main__":
    e = EscapeRoom()

    for i in range(5):
        j = Jugador(f"J{i+1}")
        j.start()
    for i in range (5):
        j.join()