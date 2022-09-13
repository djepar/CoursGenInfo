from multiprocessing import Queue

colors = ['red', 'green', 'blue', 'black']
cnt = 1

#instantiating a queue project

queue = Queue()
print('pushing items to queue:')
for color in colors:
    print('item no: ', cnt, ' ', color)
    queue.put(color)
    cnt += 1
print('\npopping items from queue:')
cnt = 0
while not queue.empty():
    print('item no: ', cnt, ' ', queue.get())
    cnt += 1



#https://www.digitalocean.com/community/tutorials/python-multiprocessing-example