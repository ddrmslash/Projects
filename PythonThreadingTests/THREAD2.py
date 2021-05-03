import time
from threading import Thread

COUNT = 500000000


def countdown(n):
    #t = 0
    while n>0:
        n -= 1
    #    t += 1
    #print(t)

t1a = Thread(target=countdown, args=(COUNT,))
#t2 = Thread(target=countdown, args=(COUNT//2,))

starta = time.time()
t1a.start()
#t2.start()

t1a.join()
#t2.join()

enda = time.time()

ended = enda - starta

print('THREAD 2 Time taken in seconds -', enda - starta)

st1 = str(starta)
en1 = str(enda)
conversion = str(ended)

f = open(r"C:\Users\goro\Desktop\PythonThreadingTests\TOTALS.txt", "a")
f.write('\n' + '\n' + "START THREAD2: " + st1 + '\n' + "END THREAD 2: " + en1 + '\n' + conversion)
f.close()