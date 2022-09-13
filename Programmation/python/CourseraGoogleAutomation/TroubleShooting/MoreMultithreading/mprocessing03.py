#https://www.youtube.com/watch?v=HxGC8y0o_Cg
"""
Queue : A FIFO data structure, Queues objects need to be pickled 
to send and unpickled to consume. It allows
interprocess communication.

It allows the Process to consume shared data when passed as a parameter. 
1. Use put to insert data to the Queue
2. Use get to consume data from the Queue
"""

import multiprocessing as mp

def sqr(x,q):
    print(x*x)

if __name__ == '__main__':
    q = mp.Queue()
    p = mp.Process(target=sqr, args=(4, q))
    p.start()
    p.join()

    result = q.get()
    print(result)
    p.end()
 
