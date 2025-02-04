import threading
import random
import time


class Aparcamiento(threading.Thread):
    espacios = 5
    semaforo = threading.Semaphore(espacios)
    espacios_libres = espacios

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        Aparcamiento.semaforo.acquire()
        Aparcamiento.espacios_libres -= 1
        print(f"El 🚙 {self.name} 🚙 entra.")
        print(f"---> Espacios disponibles: {Aparcamiento.espacios_libres} <---")
        time.sleep(random.randint(2, 10))
        Aparcamiento.espacios_libres += 1
        print(f"El 🚙 {self.name} 🚙 abandona el aparcamiento.")
        print(f"---> Espacios disponibles: {Aparcamiento.espacios_libres} <---")

        Aparcamiento.semaforo.release()

