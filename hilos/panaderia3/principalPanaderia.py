from time import sleep

from Panaderia import Comprador, Panaderia, Reponedor

if __name__ == '__main__':
    NUM_COMPRADORES = 10
    p=Panaderia()

    lista = []

    for i in range(NUM_COMPRADORES):
        lista.append(Comprador(i, p, ))


    lista.append(Reponedor(p, ))

    for c in lista:
        c.start()

    for c in lista:
        c.join()

