from threading import Thread, get_native_id, Lock
import time
glob = 0
counter = 1
def increase(L):
    with L as P:
        global counter
        print(f"Thread {get_native_id()} is entering increase. Counter={counter}")
        counter += 1
        global glob
        print(f"Thread {get_native_id()} is inside increase. Counter={counter}")
        counter += 1
        temp = glob
        print(f"Thread {get_native_id()} is inside increase. Counter={counter}")
        counter += 1
        temp += 1
        print(f"Thread {get_native_id()} is inside increase. Counter={counter}")
        counter += 1
        print(f"Thread {get_native_id()} is going to sleep. Counter={counter}")
        counter += 1
        #time.sleep(0.1)
        glob = temp
L = Lock()
t1 = Thread(target=increase, args=(L,))
t2 = Thread(target=increase, args=(L,))
print(f"main thread. Counter={counter}")
counter += 1
t1.start()
print(f"main thread. Counter={counter}")
counter += 1
t2.start()
print(f"main thread. Counter={counter}")
counter += 1
t1.join()
print(f"main thread. Counter={counter}")
counter += 1
t2.join()
print(f"main thread. Counter={counter}")