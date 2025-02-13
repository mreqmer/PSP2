from threading import *
#tabien
class Contador(Thread):
    def __init__(self):
        self.valor = 0
        self.lock = Lock()

    def incrementa(self, total):
        with self.lock:
            if self.valor >= total:
                return
            self.valor += 1
            print("+1, total: " + str(self.valor))

    def obtener_valor(self):
        return self.valor

def incrementar_contador(contador, total):
   while contador.obtener_valor() < total:
       contador.incrementa(total)

if __name__ == "__main__":
   contador = Contador()
   hilos = []
   N = 10
   TOTAL = 10000

   for _ in range(N):
       hilo = Thread(target=incrementar_contador, args=(contador, TOTAL))
       hilos.append(hilo)
       hilo.start()

   for hilo in hilos:
       hilo.join()

   print(f"Valor final del contador: {contador.obtener_valor()}")



