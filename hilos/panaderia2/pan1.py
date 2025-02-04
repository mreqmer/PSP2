from cPanaderia import Comprador, Panaderia

if __name__ == '__main__':
    p=Panaderia()
    for i in range(10):
        c = Comprador(i,p)
        c.start()