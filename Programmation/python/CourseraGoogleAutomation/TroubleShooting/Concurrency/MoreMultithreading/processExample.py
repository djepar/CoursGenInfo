from multiprocessing import Process
import time

def printcont(continent):
    num = 909999
    num2 = 9999
    for i in range(2,num2):
        num *= i
    print("The name of continent is : ", continent)
if __name__ == "__main__":
    start = time.time()
    names= ['America', 'Europe', 'Africa','Asia', 'Oceanie', 'Antartica']
    procs = []

    for name in names:
        proc = Process(target=printcont, args=(name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    end = time.time()
    print("It's took : {} seconds".format(end-start) )

#https://www.digitalocean.com/community/tutorials/python-multiprocessing-example