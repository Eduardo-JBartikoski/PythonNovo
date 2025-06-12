from threading import *;
import time;

s=Semaphore(2)

 

def example(nome,idade):

  for i in range(3):
    
      cont+ 1
      s.acquire()

      print("Olá",nome, idade)
    
      time.sleep(2)

      s.release()

      

threadA=Thread(target=example, args=("João",15))

threadB=Thread(target=example, args=("José",20))

threadC=Thread(target=example, args=("Maria",26))

threadD=Thread(target=example, args=("Ana",29))

 

threadA.start()

threadB.start()

threadC.start()

threadD.start() 