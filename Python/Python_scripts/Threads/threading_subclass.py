import threading
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print(nameOfThread, "-------------",time.time())

class MyThread(threading.Thread):
    def __init__(self,thread_name,delay):
        threading.Thread.__init__(self)
        self.thread_name=thread_name
        self.delay = delay

    def run(self):
        print("start thread",self.thread_name)
        print_epoch(self.thread_name,self.delay)
        print("end thread",self.thread_name)


if __name__ == "__main__":
    t1=MyThread("Thread_1",1)
    t2=MyThread("Thread_2",2)

    t1.start()
    t2.start()

    print(t1.getName()) #Gives the name of the thread 
    print(t2.getName())
    print(threading.active_count()) #Gives no of threads inside the program
    print(threading.currentThread()) ##GIves current thread which is active now 
    print(threading.enumerate())  ##Enumerate/gives the no of threads that are active 

    t1.join()
    t2.join()
    print("End result")