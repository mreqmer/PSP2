from threading import *
from time import sleep


class Pedido:
    pedido = Event()

class Almacen:
    inicio_trabajo = Barrier(10)

    def nuevo_pedido(self):
        while(True):
            p = Pedido
            self.pedidos.append(p)
            sleep(10)

class Trabajador(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Trabajador {self.name} preparado para trabajar")
        Almacen.inicio_trabajo.wait()

        print(f"Trabajador {self.name} está esperando por un pedido")
        Pedido.pedido.wait()

