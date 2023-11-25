import time

def fun(no):
    sum = 0
    
    for i in range(10000):
        sum = sum + (no*no)
    return sum    

def main():
    print("demonstration of serial execution using single core")

    starttime = time.time()
    
    result = []
    for no in range(10000):
        result.append(fun(no))

    endtime = time.time()
    
    print("time required to execute the apploication is : ",endtime-starttime)
    
    
if __name__ == "__main__":
    main()