import threading

def my_thread():
    print("thread is running ")

th = threading.Thread(target = my_thread)
th.start()

# import multiprocessing
# import Process

# def my_process():
#     print("thread is running ")

# th = threading.Thread(target = my_thread)
# th.start()