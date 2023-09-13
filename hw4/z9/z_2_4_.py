import requests
from multiprocessing import Process
import time
from hw4.urls import urls
from z_3_4 import download


processes = []
start_time = time.time()
if __name__ == "__main__":
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()