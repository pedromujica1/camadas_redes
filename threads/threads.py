from threading import Thread 
from time import sleep


class Contador(Thread):

    def __init__(self, n, segundos, nome):
        Thread.__init__(self)
        self.n = n
        self.segundos = segundos
        self.nome = nome
        
    def run(self):
        for i in range(self.n):
            print(i+1)
            sleep(self.segundos)
        print(f'Thread {self.nome}')
    
Contador(5,3,'James Bond').start()
Contador(10,2, 'Tom Cruise').start()
Contador(15,1, 'Peter Parker').start()

#print('Aguardando threads terminarem')
#sleep(15)
#print('Programa finalizado')