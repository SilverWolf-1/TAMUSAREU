import time
from multiprocessing import Pool

def sum_square(number):
    s=0
    for i in range(number):
        s += i*i
    return s

def sum_square_star_ver(a, b):
    time.sleep(.5)
    return (a+b) * (a+b)

if __name__ == '__main__':
    numbers = range(10)
    p = Pool()
    result = p.map(sum_square, numbers) #only accepts one argumrnt
    print(result)
    numberTuple = [(1,2),(3,4)] #arguments for the star version
    resultButWithTwoArgs = p.starmap(sum_square_star_ver, numberTuple)
    print(resultButWithTwoArgs)
    p.close()
    p.join()