# concurrency in Python

import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order {i}")
        time.sleep(1)    

def serve_orders():
    for i in range(1, 4):
        print(f"Serving order {i}")
        time.sleep(1)


# create orders taking threads

order_thread = threading.Thread(target=take_orders)
serve_orders_thread = threading.Thread(target=serve_orders)

order_thread.start() # start the thread if we will not start the thread it will not run
serve_orders_thread.start()

order_thread.join() # wait for the thread to complete if we will not use join main thread will not wait for this thread to complete
serve_orders_thread.join()  # it will wait for the thread to complete and then main thread will continue

print("All orders taken and served")