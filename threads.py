import threading

def first():
    i = 0
    while i < 50:
        print("Thread 1")
        i += 1

def second():
    j = 0
    while j < 50:
        print("Thread 2")
        j += 1

#first()
#second()

threading.Thread(target=first).start()
second()
