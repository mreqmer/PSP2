import time
from threading import *


class Empresa(Thread):
    def __init__(self, nombre, event:Event) :
        Thread.__init__(self, name=nombre)
        self.evento = event
        self.nombre = nombre


    def run(self):

        print(f"{self.nombre} inicia la venta de entradas.")
        self.evento.set()
        time.sleep(5)
        self.evento.clear()

        print(f"{self.nombre} cierra la venta de entradas")


class Comprador(Thread):
    def __init__(self, nombre, event1:Event, event2:Event) :
        Thread.__init__(self, name=nombre)
        self.evento1 = event1
        self.name = nombre
        self.evento2 = event2

    def run(self):

        while not self.evento1.is_set():
            self.evento2.wait()

        if self.evento2.is_set():
            self.evento2.set()



        if self.evento2.is_set():
            print(f"El comprador {self.name} está comprando una entrada.")
            time.sleep(3)
            print(f"Entrada comprada por {self.name}.")
            evento.clear()

if __name__ == '__main__':
    evento = Event()
    fila = Event()
    empresa = Empresa("Concietos", evento)

    compradores = [Comprador(f"Comprador {i + 1}", evento, fila) for i in range(5)]

    empresa.start()

    for comprador in compradores:
        comprador.start()

    for comprador in compradores:
        comprador.join()




