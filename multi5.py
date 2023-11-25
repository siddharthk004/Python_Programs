import multiprocessing
import os

def task1(value):
    print("Executing the firsgt task...")
    for i in range(value):
        print("task1 : ",i)
    
    
def task2(value):
    print("Executing the second task...")
    for i in range(value):
        print("task2 : ",i)
      
def main():
    print("demonstration of multiprocessing")
    
    print("PID of running process is : ",os.getpid())
    
    no1 = 5
    no2 = 8
    
    p1 = multiprocessing.Process(target=task1 , args = (no1,))
    p2 = multiprocessing.Process(target = task2 , args = (no2,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
if __name__ == "__main__":
    main()