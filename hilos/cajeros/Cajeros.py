import threading
import random
import time


class Cajeros(threading.Thread):
    cajeros = 3
    semaforo = threading.Semaphore(cajeros)
    cajeros_libres = cajeros

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        Cajeros.semaforo.acquire()
        print(f"El cliente {self.name}  entra al cajero.")
        Cajeros.cajeros_libres -=1



