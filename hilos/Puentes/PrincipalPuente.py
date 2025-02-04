import time
import random

from Puentes.Puente import Puente

if __name__ == '__main__':

    for i in range(10):
        vehiculo = Puente(f"Vehículo-{i + 1}", random.randint(0, 1))
        vehiculo.start()
        random.randint(1,5)




