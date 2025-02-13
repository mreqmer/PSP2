import random
from threading import *

class Adivina:
    numero = random.randint(1, 100)  # Número a adivinar
    acertado = False  # Bandera que indica si se ha adivinado
    cond = Condition()  # Condición para sincronización

class Adivinador(Thread):
    def __init__(self, nombre, adivina):
        super().__init__(name=nombre)
        self.adivina = adivina

    def run(self):
        while True:
            with self.adivina.cond:
                if self.adivina.acertado:
                    break  # Si ya se ha acertado, el hilo termina
                intento = random.randint(1, 100)
                print(f"{self.name} ha generado el número {intento}")
                if intento == self.adivina.numero:
                    self.adivina.acertado = True
                    print(f"{self.name} ha acertado el número {self.adivina.numero}!")
                    self.adivina.cond.notify_all()  # Notificar a los demás hilos que se ha acertado
                    break  # Terminar ejecución del hilo
                else:
                    print(f"{self.name} no era el número.")

if __name__ == "__main__":
    ad = Adivina()  # Instanciamos la clase Adivina que tiene el número a adivinar

    hilos = []
    for i in range(10):  # Creamos 10 hilos
        t = Adivinador(f"Hilo-{i}", ad)
        t.start()
        hilos.append(t)

    for hilo in hilos:  # Esperamos a que todos los hilos terminen
        hilo.join()
