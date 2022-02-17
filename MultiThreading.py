from concurrent.futures import thread
import threading
from queue import Queue
import time
import os


fila_threads = Queue()
items = [5, 10, 15, 20, 25]
thread_fila_condition = threading.Condition()


def thread_cond(cond):
    with cond:
        while fila_threads.empty():
            print("Thread status Aguardando: ", threading.current_thread().name)
            print("Thread PID: ", os.getpid())
            print("Main_Thread: ", threading.current_thread().ident)

            cond.wait()
        else:
            value = fila_threads.get()

        print("Nome da Thread: ", threading.current_thread().name)


def thread_fila(cond):
    time.sleep(2)

    print("Thread Current: ", threading.current_thread().name)
    print("Thread PID: ", os.getpid())
    print("Thread Current Ident: ", threading.current_thread().ident)

    with cond:
        for item in items:
            fila_threads.put(item)

            print("Notifica as Threads, muda de wait para run...")
            cond.notifyAll()


for i in range(len(items)):
    threads = threading.Thread( daemon=False, target=thread_cond, args=(thread_fila_condition,))
    threads.start()


startFila = threading.Thread(name='queue_task_thread', daemon=False, target=thread_fila, args=(thread_fila_condition,))
startFila.start()
