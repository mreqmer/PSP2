import random
from threading import *


class NumeroOculto(Thread):
   numero = 20
   encontrado = False
   bloqueo = Lock()
   def __init__(self):
       Thread.__init__(self)


class Adivinador(Thread):
   def __init__(self, nombre):
       Thread.__init__(self, name=nombre)
       self.intento = 0
   def run(self):
       while True:
           with NumeroOculto.bloqueo:
               if NumeroOculto.encontrado:
                   break
               else:
                   self.intento = random.randint(1, 100)
                   print(f"{self.name} intentó: {self.intento}")
                   if NumeroOculto.numero == self.intento:
                       NumeroOculto.encontrado = True
                       print(f"{self.name} encontró el {self.intento}!!!!!!")




if __name__ == '__main__':
   numero_oculto = NumeroOculto()


   for i in range(10):
       p=Adivinador(i)
       p.start()
   for i in range(10):
       p.join()
