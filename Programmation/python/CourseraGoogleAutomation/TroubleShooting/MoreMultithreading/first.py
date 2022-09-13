import time
import multiprocessing


start = time.perf_counter()
processes = []

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")

for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    p.processes.append(p)

for process in processes:
    process.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')