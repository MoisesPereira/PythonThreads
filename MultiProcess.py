from asyncio.log import logger
from cmath import log
import sys, logging, time, os, random
from multiprocessing import Process, Queue, Pool,\
    cpu_count, current_process, Manager


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
format = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(format)
logger.addHandler(ch)


fila_process = Queue()
cpus = cpu_count()
manager = Manager()
items = [5, 10, 15, 20, 25, 30, 35, 40]


def set_fila(fila, item):
    print(f"SET FILA - NUMERO PROCESSO: ", os.getpid())
    logger.info("Processo: {current_process().name}, Valor: {items[item]}")
    fila.put(items[item])


def get_fila(fila):
    print("GET FILA - NUMERO PROCESSO: ", os.getpid())
    while not fila.empty():
        value = fila.get()


for i in range(cpus):
    producer = Process(target=set_fila, args=(fila_process, i))
    producer.start()
producer.join()

time.sleep(1)

consumer_list = []
for i in range(cpus):
    consumer = Process(target=get_fila, args=(fila_process,))
    consumer.start()
    consumer_list.append(consumer)

[consumer.join() for consumer in consumer_list]    

