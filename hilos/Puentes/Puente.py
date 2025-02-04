import threading
import random
import time


class Puente(threading.Thread):
    semaforoNorte = threading.Semaphore(1)
    semaforoSur = threading.Semaphore(1)

    def __init__(self, nombre, direccion):
        threading.Thread.__init__(self, name=nombre)
        self.direccion = direccion
    def run(self):
        if(self.direccion == 0):
            Puente.semaforoNorte.acquire()
            print(f"{self.name} pasando hacia el norte.")
            time.sleep(random.randint(1,3))
            Puente.semaforoNorte.release()
            print("Via norte libre")
        else:
            Puente.semaforoSur.acquire()
            print(f"{self.name} pasando hacia el sur.")
            time.sleep(random.randint(1, 3))
            Puente.semaforoSur.release()
            print("Via sur libre")

