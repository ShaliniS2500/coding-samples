import threading
import time
from multiprocessing import Process

def my_function():
    for i in range(5000):
        for j in range(5000):
            pass

start = time.time()
# my_function()
# my_function()
# print(f"Execution time: {time.time() - start:.2f}s")

# t1 = threading.Thread(target=my_function)
# t2 = threading.Thread(target=my_function)
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

p1 = Process(target=my_function)
p2 = Process(target=my_function)

p1.start()
p2.start()
p1.join()
p2.join()

print(f"Execution time: {time.time() - start:.2f}s")

