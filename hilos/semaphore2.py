import random
from threading import Semaphore, Thread
import time

class Supermercado(Thread):

    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        print("Hilo", self.name, " va a una caja")
        Supermercado.semaforo.acquire()
        print("Hilo", self.name, " está siendo atendido")
        time.sleep(random.randint(1,10))
        print("Hilo", self.name, " está pagando")
        Supermercado.semaforo.release()
        print("Hilo, ", self.name, " abandona el supermercado")

if __name__ == '__main__':
    for i in range(0, 10):
        s = Supermercado(i)
        s.start()