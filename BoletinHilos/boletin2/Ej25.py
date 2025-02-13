from random import randint
from threading import *
from time import sleep


class Libreria:
    libros = [False] * 9
    prestado = Condition()

class Estudiante(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
        self.libro1 = randint(0,8)
        self.libro1_adquirido = False
        self.libro2 = self.busca_libro2()
        self.libro2_adquirido = False

    def busca_libro2(self):
        numero = randint(0, 8)
        while (numero == self.libro1):
            numero = randint(1, 9)
        return numero

    def run(self):
        while not self.libro1_adquirido and not self.libro2_adquirido:
            print(f"Estudiante {self.name} esperando por los libros {self.libro1} y {self.libro2}")
            with Libreria.prestado:
                while Libreria.libros[self.libro1]:
                    print(f"Estudiante {self.name} esperando por el libro {self.libro1}")
                    Libreria.prestado.wait()
                while Libreria.libros[self.libro2]:
                    print(f"Estudiante {self.name} esperando por el libro {self.libro1}")
                    Libreria.prestado.wait()

            Libreria.libros[self.libro1] = True
            self.libro1_adquirido = True
            self.libro2_adquirido = True
            Libreria.libros[self.libro2] = True
            print(f"Estudiante {self.name} leyendo los libros {self.libro1} y {self.libro2}")
            sleep(randint(1,9))

            with Libreria.prestado:
                Libreria.libros[self.libro1] = False
                Libreria.libros[self.libro2] = False
                Libreria.prestado.notify_all()

if __name__ == '__main__':
    l = Libreria()

    for i in range(1,5):
        e = Estudiante(f"E{i}")
        e.start()
    for i in range(1,5):
        e.join()




