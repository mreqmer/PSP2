from random import randint
from threading import *
from time import sleep


"""
Ejercicio para manejar la producción de una fabrica de aceite
Se usan dos lock, uno para manejar que se pueda crear aceite si la tolva no está llena y otro para manejar que la tolva
tiene algo de aceite y se pueda embotellar
"""
class Fabrica(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.capacidad_maxima = 500
        self.capacidad = 0
        self.bloqueo_tolva = Lock()
        self.bloqueo_tolva_minimo = Lock()
    def run(self):
        while(True):
            if self.capacidad >= self.capacidad_maxima:
                self.bloqueo_tolva.acquire()
            elif self.bloqueo_tolva.locked() and self.capacidad < self.capacidad_maxima:
                self.bloqueo_tolva.release()

            if self.capacidad <= 0:
                self.bloqueo_tolva_minimo.acquire()
            elif self.capacidad >=5:
                self.bloqueo_tolva_minimo.release()



class Operario(Thread):
    def __init__(self, nombre, fabrica:Fabrica):
        Thread.__init__(self, name = nombre)
        self.fabrica = fabrica
    def aporta_aceite(self):
        cantidad = randint(1, 6)
        cantidad_total = cantidad * 5
        sleep(cantidad)
        return cantidad_total

    def run(self):
        sleep(1)
        while(True):
            if not self.fabrica.bloqueo_tolva.locked():
                cantidad_generada = self.aporta_aceite()
                self.fabrica.capacidad += cantidad_generada
                print(f"El Operario {self.name} ha generado {cantidad_generada} de aceite. {self.fabrica.capacidad}")



class LineaEmbotellado(Thread):
    def __init__(self, nombre, fabrica:Fabrica):
        Thread.__init__(self, name=nombre)
        self.fabrica = fabrica

    def embotellado_aceite(self):
        self.fabrica.capacidad -= 5
        print(f"La linea {self.name} ha generado 1 botella. {self.fabrica.capacidad}")
        sleep(0.5)

    def run(self):

        while (True):
            if not self.fabrica.bloqueo_tolva_minimo.locked():
                self.embotellado_aceite()




if __name__ == '__main__':
    f = Fabrica()
    f.start()

    for i in range(2):
        l = LineaEmbotellado(f"L{i + 1}", f)
        l.start()
    for i in range(4):
        o = Operario(f"O{i+1}", f)
        o.start()



