# From  https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
import time
import asyncio

async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)

startTime = time.time() 
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(do_some_work(2)),asyncio.ensure_future(do_some_work(5))]

loop.run_until_complete(asyncio.gather(*tasks))
completeTime = time.time() - startTime
print("The program took in total : {0} ".format(completeTime))