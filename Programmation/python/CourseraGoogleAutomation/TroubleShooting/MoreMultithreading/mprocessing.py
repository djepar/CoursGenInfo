from multiprocessing import Process
import multiprocessing as mp
print(mp.cpu_count())

def myfunc():
    print("Hello World")

if __name__ == "__main__":
    proc = Process(target=myfunc)
    proc.start()
    proc.join()