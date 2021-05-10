import threading

x = 0

def thread_task(lock):
    global x
    for i in range(1000000):
        lock.acquire()  #It locks the value of the shared resource 
        x += 1
        lock.release()
    
## In the above case only one thread can access the shared resource ( x ) and other thread can access the data only if current thread is released.

def main_task():

    lock = threading.Lock()

    t1=threading.Thread(target=thread_task,args=(lock,))
    t2=threading.Thread(target=thread_task,args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print(x)

