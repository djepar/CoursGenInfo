from multiprocessing import Process
import time

def weirdStuff(anum):
    new = 409
    new = (new * anum * (anum ** 0.5) - (anum ** 0.5 - 100))
    for x in range(1,999):
        new += x
    for x in range(1,100):
        new *= x
    new2 = 1
    new3 = 0
    for i in range(1, 9999):
        if i % 2 == 0:
            for i in range(9999):
                new2 += i
        elif i % 3 == 0:
            for i in range(9999):
                new3 -= i
        elif i % 4:
            if new3 != 0:
                new2 / new3
        elif i % 5:
                if new2 != 0:
                 new3 / new2
        else:
            new2 - new3
        
    print("The number is ", new, new2, new3)



if __name__ == "__main__":

    nums = [99999, 88888, 77777]

    start = time.time()
    for num in nums:
        weirdStuff(num)

    end = time.time()
    print("The program took {} seconds without multi".format(end-start))

    
    
    start2 = time.time()
    procs = []

    for num in nums:
        proc = Process(target=weirdStuff, args=(num,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    end2 = time.time()
    print("It's too : {} second with multi".format(end2-start2))