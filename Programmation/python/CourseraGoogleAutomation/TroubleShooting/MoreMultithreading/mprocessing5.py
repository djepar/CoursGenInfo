


"""
Multiprocessing 
Module even improved in Python3.8
Introduced Shared Memory class
Provides much faster way to pass data. 
Its segments can be allocated as raw regions of bytes. 
"""
"""
Pool = Data Parallelism
Pool : Help us to execute a function against multiple input values in parallel. 
"""

from multiprocessing import Pool
import time
tasks = (["A", 5], ["B", 2], ["C", 1], ["D", 3])

def tasks_exec(tasks_data):
    print(f'Process {tasks_data[0]} waiting {tasks_data[1]} seconds')
    time.sleep(int(tasks_data[1]))
    print(f'Process {tasks_data[1]} finished')
def pool_func():
    p = Pool(2)
    p.map(tasks_exec, tasks)

if __name__ == '__main__':
    pool_func()