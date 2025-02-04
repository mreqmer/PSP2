import time
import random

from cine.SalaCine import SalaCine

if __name__ == '__main__':

    for i in range(20):
        espectador = SalaCine(f"Espectador-{i + 1}")
        espectador.start()
        time.sleep(random.randint(1, 3))