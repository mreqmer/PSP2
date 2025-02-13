from random import randint
from threading import *
from time import sleep




class Carniceria:
   dependientes = 4
   cajas = Semaphore(dependientes)


class Cliente(Thread):
   def __init__(self, nombre):
       Thread.__init__(self, name=nombre)


   def run(self):
       print(f"{self.name} entra en la carnicería")
       with Carniceria.cajas:
           print(f"Cliente {self.name} es atendido")
           sleep(randint(1, 10))
           print(f"Cliente {self.name} ha salido")




if __name__ == '__main__':


   c = Carniceria()


   for i in range(10):
       cliente = Cliente(i+1)
       cliente.start()


   for i in range(10):
       cliente.join()
