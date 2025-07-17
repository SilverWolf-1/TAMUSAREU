import multiprocessing
import time


def worker(num): # type: ignore
    print(f"Worker {num} starting")
    time.sleep(2)
    print(f"Worker {num} done")

def main():
    processes = []

    for i in range (10000):
        x=i+1
        p = multiprocessing.Process(target=worker, args=(x,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
if __name__ == "__main__":
    main()