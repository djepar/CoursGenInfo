## Running  a loop in a different thread

from threading import Thread
import asyncio
import time

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

startTime = time.time()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
endTime = time.time() - startTime
print("The program took in total : {0} ".format(endTime))