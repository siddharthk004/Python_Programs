import time
import multiprocessing

def fun(no):
    sum = 0
    
    for i in range(10000):
        sum = sum + (no*no)
    return sum    

def main():
    print("demonstration of serial execution using multi core")

    starttime = time.time()
    p = multiprocessing.Pool()
    result = []
    result = p.map(fun,range(10000))
    p.close()
    p.join()
    
    endtime = time.time()
    
    print("time required to execute the apploication is : ",endtime-starttime)
    
    
if __name__ == "__main__":
    main()