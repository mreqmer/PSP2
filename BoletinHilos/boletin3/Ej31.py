from random import randint
from threading import *
from time import sleep


def correr(nombre_corredor):
    tiempo_carrera = randint(1,9)

    sleep(tiempo_carrera)

    print(f"{nombre_corredor} terminó de correr. Tardó {tiempo_carrera}s")

if __name__ == '__main__':

    for i in range(10):
        temporizador = Timer(3, correr, args=(f"C{i}",))
        temporizador.start()
    for i in range(3):
        print(3 - i)
        sleep(1)




