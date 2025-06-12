"""
import _thread

def atividade(nome_atividade):
    print ("thread : %s" % (nome_atividade))

_thread.start_new_thread(atividade, ("tarefa 1",))
_thread.start_new_thread(atividade, ("tafera 2",))

while True:
    pass

"""
"""
import _thread
import time

max_loop = 5

def atividade(nome_atividade,espera):
    global max_loop
    contador = 0
    while contador < max_loop:
        time.sleep(espera)
        print("thread : %s" % (nome_atividade))
        contador +=1

_thread.start_new_thread(atividade, ("Tarefa 1", 10))
_thread.start_new_thread(atividade, ("Tarefa 2", 20))
"""
import _thread
import time

num_thread = 0
thread_iniciada = False
max_loop = 5

def atividade(nome_atividade, espera):
    global num_thread, max_loop, thread_iniciada
    thread_iniciada = True
    num_thread += 1
    contador = 0
    while contador < max_loop:
        time.sleep(espera)
        print("Thread : %s" % (nome_atividade))
        contador += 1
    num_thread -= 1

_thread.start_new_thread(atividade, ("Tarefa 1", 10))
_thread.start_new_thread(atividade, ("Tarefa 2", 20))

while not thread_iniciada:
    pass
while num_thread > 0:
    pass