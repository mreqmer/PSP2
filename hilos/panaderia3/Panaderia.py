import threading
import time
import random



class Panaderia(threading.Thread):
    capacidad = 7
    barras = 7
    # venta= threading.Lock()
    con = threading.Condition()

    def __init__(self):
        threading.Thread.__init__(self)

    def venta_pan(self):
        with Panaderia.con:
            while(Panaderia.barras==0):
                print("No se puede vender, REPONIENDO")
                Panaderia.con.wait()

            Panaderia.barras -= 1
            print(f"Se vendió un pan. Panes restantes: {Panaderia.barras}")
            Panaderia.con.notify_all()

    def repone_pan(self):
        with Panaderia.con:
            while(Panaderia.barras > 0):
                print("Cesta de pan LLENA")
                Panaderia.con.wait()

            Panaderia.barras = 7
            print(f"Se repone el pan.")
            Panaderia.con.notify_all()


class Comprador(threading.Thread):
    def __init__(self, nombre, panaderia):
        threading.Thread.__init__(self, name=nombre)
        self.nombre=nombre
        self.panaderia = panaderia

    def run(self):
        while(True):
            time.sleep((random.uniform(0.5, 2)))
            print(f"Comprador {self.nombre} intenta comprar pan.")
            self.panaderia.venta_pan()



class Reponedor(threading.Thread):
    def __init__(self, panaderia):
        threading.Thread.__init__(self)
        self.panaderia = panaderia

    def run(self):
        while (True):
            time.sleep((random.uniform(0.5, 2)))
            self.panaderia.repone_pan()





