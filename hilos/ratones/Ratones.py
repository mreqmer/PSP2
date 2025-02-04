import time
from random import *
from threading import *


# Los ratones tienen que compartir el plato
class Raton(Thread) :
    def __init__(self, nombre, event:Event) :
        Thread.__init__(self, name=nombre)
        self.evento = event
        self.name = nombre

    def run(self):
#EI ratón espera a que eI plato se quede libre
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print("E1 ratón",self.name, "toma eI control del plato")
        time.sleep(2)
        print("E1 ratón",self.name, "termina de comer")
        self.evento.set()

if __name__ == '__main__':
    evento = Event()
    evento.set()
    ratones = [Raton("Raton " + str(i), evento) for i in range(3)]
    for raton in ratones:
        raton.start()

    for raton in ratones:
        raton.join()
