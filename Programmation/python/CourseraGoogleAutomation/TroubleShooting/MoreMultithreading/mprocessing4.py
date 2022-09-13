#https://www.youtube.com/watch?v=HxGC8y0o_Cg
import multiprocessing as mp

def sqr(x,q):
    print(x*x)

if __name__ == '__main__':
    q = mp.Queue()
    processes  = [mp.Process(target=sqr, args=(i,q)) for i in range(2,10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    result = [q.get() for p in processes]
    print(result)    

