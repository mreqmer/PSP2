from threading import *

class Texto(Thread):
    bloqueo = Lock()
    texto = "La tarara lleva un vestido blanco lleno cascabeles"
    def __init__(self):
        Thread.__init__(self)

class CuentaVocal(Thread):
    def __init__(self, nombre, vocal):
        Thread.__init__(self, name=nombre)
        self.contador = 0
        self.vocal = vocal


    def run(self):
        Texto.bloqueo.acquire()
        for letra in Texto.texto:
            if letra == self.vocal:
                self.contador += 1

        print("Hay " + str(self.contador) + " " +  self.vocal )
        Texto.bloqueo.release()

if __name__ == "__main__":
    tx = Texto()
    vocales = ["a", "e", "i", "o", "u"]
    for i in range (5):
        cosa = CuentaVocal(i+1, vocales[i])
        cosa.start()



