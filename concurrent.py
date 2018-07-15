from concurrent.futures import ThreadPoolExecutor
import time

global HH
HH = 0

global st
st = False

def m1():
    global st
    while True:
        global HH
        HH += 1
        if st:
            break


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(m1)


try:
    while True:
        print (HH)
        time.sleep(1)
except KeyboardInterrupt:
    st = True
