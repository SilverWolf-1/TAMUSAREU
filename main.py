import asyncio

async def taskA(): #start and ending of conversation
    print("Hey")
    await asyncio.sleep(5)
    print("here.")

async def taskB(): #middle dialogue of conversation
    print("I just finished practice.")
    await asyncio.sleep(1)
    print("Where are you?")


#main
async def main():
    await asyncio.gather(taskA(), taskB())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Tasks executed in {elapsed:0.1f} seconds")