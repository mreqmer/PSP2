from random import randint
from threading import *
from time import sleep




class Panaderia():
   dependientes = 1
   dependiente = Semaphore(dependientes)


class Cliente(Thread):
   def __init__(self, nombre):
       Thread.__init__(self, name=nombre)


   def run(self):
       print(f"Cliente {self.name} entra a la panaderia")
       with Panaderia.dependiente:
           print(f"Cliente {self.name} está comprando pan")
           sleep(randint(3,5))
           print(f"Cliente {self.name} ha comprado el pan")




if __name__ == '__main__':


   p = Panaderia()


   for i in range(10):
       sleep(randint(1,5))
       c = Cliente(i)
       c.start()
   for i in range(10):
       c.join()
