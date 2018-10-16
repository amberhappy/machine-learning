import threading
import time
from queue import Queue

def job(L,q):
    for i in range(len(L)):
        L[i] = L[i]**2
    q.put(L)

def multithreading():
    q = Queue()
    threads = []
    data =[[1,1,4],[5,7,8],[3,4,8],[42,5,6]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        result.append(q.get())
    print(result)
if __name__ =="__main__":
    multithreading()