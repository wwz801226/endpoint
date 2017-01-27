import threading
import time

def sayhello():
    print(threading.active_count())
    worker()
    global t    #Notice: use global variable!
    t = threading.Timer(5.0, sayhello)
    t.start()

def worker():
    a = threading.Thread(target=aaa)
    print(str(time.time())+' '*5+a.getName()+' '*5+'begain')
    #print('a'+a.getName())
    a.start()

def aaa():
    begain = time.time()
    for i in range(1,100000000):
        i+=1
    #time.sleep(60)
    end = time.time()
    print("I'am"+ " "*5 + threading.current_thread().getName())
    print(end-begain)
    if threading.current_thread().getName() == 'Thread-8':
        b = 1/0
        print(b)


if __name__ =="__main__":

    # t = threading.Timer(5.0, sayhello)
    # t.start()
    #######################################################################
    i=1
    while True:
        print(threading.active_count())
        print(time.time())
        time.sleep(5)

        worker()
        i+=1



