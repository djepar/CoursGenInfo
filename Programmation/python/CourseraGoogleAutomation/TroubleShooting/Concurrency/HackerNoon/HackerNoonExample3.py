# Thread safe alternative

import time 

import asyncio
def more_work(x): 
    print("More work %s" % x)
    time.sleep(x)
    print("Finished more work %s" % x)

startTime = time.time()
new_loop = asyncio.new_event_loop()
new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work,3)


endTime = time.time() - startTime
print("The program took in total : {0} ".format(endTime))