import time
import threading

start = time.time()

def print_squares(num):
    sum = 0 
    for i in range(0,num+1):
        sum = sum + i**2 
        print("Square : ",sum)
    print(sum)


def print_cubes(num):
    sum1 = 0 
    for i in range(0,num+1):
        sum1 = sum1 + i**3
        print("Cube : ",sum1)
    print(sum1)

if __name__ == "__main__":
    t1=threading.Thread(target=print_squares,args=(1234,))
    t2=threading.Thread(target=print_cubes,args=(1234,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
# print_squares(1234)
# print_cubes(1234)


print("Duration is  :", time.time()-start)

