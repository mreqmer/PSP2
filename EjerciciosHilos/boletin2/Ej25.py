from random import randint
from threading import *




class Libro:
   prestado = Lock()
   def __init__(self, nombre):
       self.nombre = nombre


class Libreria:
   libros = []
   for i in range(9):
       libros.append(Libro(f"Libro {i}"))




class Estudiante(Thread):


   def __init__(self, nombre):
       Thread.__init__(self, name = nombre)
       self.libro1 = randint(1, 9)
       self.libro2 = self.busca_libro2()


   def busca_libro2(self):
       numero = randint(1, 9)
       while(numero == self.libro1):
           numero = randint(1, 9)
       return numero


   def run(self):
       print(self.name + " Se ha pedido el libro " + str(self.libro1) + " y " + str(self.libro2))


       while Libreria.libros[self.libro1 - 1].prestado.locked() and Libreria.libros[self.libro2 - 1].prestado.locked():
          if Libreria.libros[self.libro1-1].prestado.locked():
              print("Esperando por el libro " + str(self.libro1))
          else:
               Libreria.libros[self.libro1 - 1].prestado.acquire()
               print(self.name + " tiene el libro " + str(self.libro1))
          if Libreria.libros[self.libro2 - 1].prestado.locked():
              print("Esperando por el libro " + str(self.libro2))
          else:
              Libreria.libros[self.libro2 - 1].prestado.acquire()
              print(self.name + " tiene el libro " + str(self.libro1))

if __name__ == '__main__':
   libreria = Libreria()


   for i in range(4):
       estudiante = Estudiante("Estudiante " + str(i) + " :")
       estudiante.start()


   for i in range(4):
       estudiante.join()
