#https://www.youtube.com/watch?v=CRJOQtaRT_8
from multiprocessing import Process

def lang_func(lang):
    print(lang)

if __name__ == '__main__':
    langs = ['C', 'Python', 'Java', 'PHP']
    processes = []
    for l in langs:
        proc = Process(target=lang_func, args=(l,))
        processes.append(proc)
        proc.start()
    for p in processes:
        p.join()    