import process_sim
import time
import multiprocessing as mp
from multiprocessing import Process, Queue, Pool, Manager, Pipe


if __name__ == "__main__":
    q = Queue()
    p = Process(target=process_sim.start_process, args=(q,))
    p.start()
    while(1):
        time.sleep(1)
        print("B")
