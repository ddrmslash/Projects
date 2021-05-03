import time
from threading import Thread

COUNT = 500000000


def countdown(n):
    #t = 0
    while n>0:
        n -= 1
        #t += 1
    #print(t)

t1 = Thread(target=countdown, args=(COUNT,))
#t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
#t2.start()

t1.join()
#t2.join()

end = time.time()

ended = end - start

print('THREAD 3 Time taken in seconds -', end - start)

st1 = str(start)
en1 = str(end)
conversion = str(ended)

f = open(r"C:\Users\goro\Desktop\PythonThreadingTests\TOTALS.txt", "a")
f.write('\n' + '\n' + "START THREAD 3: " + st1 + '\n' + "END THREAD 3: " + en1 + '\n' + conversion)
f.close()