from random import *
from threading import *
from time import sleep




class Carniceria:
   carniceria_dependientes = 4
   carniceria_cajas = Semaphore(carniceria_dependientes)


class Charcuteria:
   charcuteria_dependientes = 2
   charcuteria_cajas = Semaphore(charcuteria_dependientes)


class Cliente(Thread):
   carne_comprada = False
   charcuteria_comprada = False
   def __init__(self, nombre):
       Thread.__init__(self, name=nombre)


   def compra_carne(self):
       print(f"{self.name} está siendo atendido en CARNICERIA")
       sleep(randint(1,10))
       print(f"{self.name} fue atendido en CARNICERIA")
       self.carne_comprada = True


   def compra_charcuteria(self):
       print(f"{self.name} está siendo atendido en CHARCUTERIA")
       sleep(randint(1,10))
       print(f"{self.name} fue atendido en CHARCUTERIA")
       self.charcuteria_comprada = True


   def run(self):
       print(f"Entra el cliente {self.name}")
       while not (self.carne_comprada and self.charcuteria_comprada):
           if(not self.carne_comprada):
               with Carniceria.carniceria_cajas:
                   self.compra_carne()
           if(not self.charcuteria_comprada):
               with Charcuteria.charcuteria_cajas:
                   self.compra_charcuteria()


if __name__ == '__main__':
   carniceria = Carniceria()
   charcuteria = Charcuteria()


   for i in range(1,10):
       cliente = Cliente(i+1)
       cliente.start()
   for i in range(1,10):
       cliente.join()
