import threading

class MiThread(threading.Thread):
        def __init__(self, num):
            threading.Thread.__init__(self)
            self.num = num

        def run(self):
            print("Soy el hilo ", self.num)