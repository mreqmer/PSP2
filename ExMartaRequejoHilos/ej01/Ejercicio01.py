from random import randint
from threading  import *
from time import sleep

"""
Ejercicio de simulación de una fabrica de agua a partir de moléculas.
Para el control de la Fábrica se ha usado un Condition para que la fabrica no genere más oxígeno o más hidrógeno de la cuenta.
Para los Trabajadores se usa Lock para que no puedan tomar más moléculas de las que deben.
"""
"""
Clase donde se generan los átomos  y se controla que se tomen
"""
class Fabrica(Thread):

    cond = Condition()

    def __init__(self, trabajadores):
        Thread.__init__(self)
        self.hidrogeno = 0
        self.oxigeno = 0
        self.trabajadores = trabajadores

    """
    Método para que un trabajador tome hidrógeno si existe
    """
    def tomar_hidrogeno(self):
        if(self.hidrogeno > 0):
            self.hidrogeno -= 1
        else:
            print("No queda hidrógeno")

    """
    Método para que un trabajador tome oxígeno si existe
    """
    def tomar_oxigeno(self):
        if (self.oxigeno > 0):
            self.oxigeno -= 1
        else:
            print("No queda oxígeno")

    def run(self):
        #Se generan átomos de forma indefinida siempre y cuando los trabajadores los vayan tomando
        while(True):
            with Fabrica.cond:
                while self.hidrogeno < self.trabajadores * 2:

                    self.hidrogeno += 1
                    print(f"Se genera hidrógeno: {self.hidrogeno}")
                    randint(2, 5)

                while self.oxigeno < self.trabajadores:
                    self.oxigeno += 1
                    print(f"Se genera oxígeno: {self. oxigeno}")
                    randint(1, 3)

"""
Clase donde se toman los átomos y se crean las moléculas
"""
class Trabajador(Thread):
    molecula_terminada = Lock()

    def __init__(self, nombre, fabrica : Fabrica):
        Thread.__init__(self, name=nombre)
        self.Fabrica = fabrica
        self.cantidad_hidrogeno = 0
        self.cantidad_oxigeno = 0

    """
    Simula el tiempo que tardaría el trabajador en llevar la molécula terminada y notificarlo
    """
    def entregar_molecula(self):
        print(f"{self.name} terminó una molécula de H2O. H{self.cantidad_hidrogeno}, O{self.cantidad_oxigeno}")
        sleep(1)
        self.cantidad_oxigeno = 0
        self.cantidad_hidrogeno = 0


    def run(self):
        #Tiempo de entrada de los trabajadores
        sleep(randint(2,10))
        print(f"Trabajador {self.name} termina su pausa del café y empieza a trabajar")
        #Los trabajadores trabajan de forma indefinida
        while(True):
            with Trabajador.molecula_terminada:
                while self.cantidad_hidrogeno < 2:
                    self.Fabrica.tomar_hidrogeno()
                    self.cantidad_hidrogeno += 1
                    print(f"Trabajador {self.name} toma hidrógeno de la fabrica")
                    sleep(1)
                while self.cantidad_oxigeno < 1:
                    self.Fabrica.tomar_oxigeno()
                    self.cantidad_oxigeno += 1
                    print(f"Trabajador {self.name} toma oxígeno de la fabrica")
                    sleep(1)
            self.entregar_molecula()




if __name__ == '__main__':

    cantidad_trabajadores = 10

    f = Fabrica(cantidad_trabajadores)

    for i in range(cantidad_trabajadores):
        t = Trabajador(f"T{i+1}", f)
        t.start()
    for i in range(cantidad_trabajadores):
        t.join()