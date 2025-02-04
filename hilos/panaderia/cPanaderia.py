import threading
import time


class Panaderia(threading.Thread):
    barras = 7
    venta= threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)

    def compra_pan(self):
        Panaderia.venta.acquire()
        if(Panaderia.barras>0):
            Panaderia.barras = Panaderia.barras - 1
            ok = True
        else:
            print("No queda pan")
            ok = False
        Panaderia.venta.release()
        return ok


class Comprador(threading.Thread):
    def __init__(self, nombre, panaderia):
        threading.Thread.__init__(self, name=nombre)
        self.nombre=nombre
        self.tiendaHabitual = panaderia

    def run(self):
        print("Soy el hilo", self.nombre, "comprando pan")
        if(self.tiendaHabitual.compra_pan()):
            print("El hilo", self.nombre, "ha comprado pan")
