from hilo1 import MiThread

print ("Soy el hilo principal")

for i in range(0, 20):
    t = MiThread(i)
    t.start()