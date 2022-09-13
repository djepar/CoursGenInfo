from multiprocessing import Process
list = [x for x in range(99999, 9999999)]
def division(num):
    for el in list:
        el = el // 4
        num = num ** el 
    return num
if __name__ == "__main__":
    numList = [999999, 99999999, 12 ,15, 16]
   
    procs = []
    proc = Process(target=division, args=(numList))
    procs.append(proc)
    proc.start


    for proc in procs:
        proc.join()