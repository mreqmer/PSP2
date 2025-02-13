from threading import *
from time import sleep

#ta mal
class Clase(Thread):
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def claseCosa(self):
        print("Soy " + self.name + " y estoy trabajando.")
        Clase.bloqueo.acquire()
        sleep(2)

        print("Soy " + self.name + " y he terminado de trabajar")
        Clase.bloqueo.release()

if __name__ == "__main__":
    ...