import time
import random

from vehiculos.vehiculosHilo import Aparcamiento

if __name__ == '__main__':

    for i in range(10):
        vehiculo = Aparcamiento(f"Vehículo-{i + 1}")
        vehiculo.start()
        time.sleep(random.randint(1, 3))