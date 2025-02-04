import threading
import random
import time


class SalaCine(threading.Thread):
    asientos = 20
    semaforo = threading.Semaphore(asientos)
    asientos_libres = asientos


    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        SalaCine.semaforo.acquire()
        SalaCine.asientos_libres -= 1
        print(f"El espectador {self.name}  entra.")
        print(f"---> Asientos disponibles: {SalaCine.asientos_libres} <---")
        time.sleep(random.randint(2, 10))
        SalaCine.asientos_libres += 1
        print(f"El especto {self.name} abandona la sala.")
        print(f"---> Asientos disponibles: {SalaCine.asientos_libres} <---")

        SalaCine.semaforo.release()
