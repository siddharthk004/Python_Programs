import multiprocessing
import os

def task1(value):
    print("Executing the firsgt task...")
    print("PID of running process for task 1 : ",os.getpid())
    
    
def task2(value):
    print("Executing the second task...")
    print("PID of running process for task 2: ",os.getpid())
      
def main():
    print("demonstration of multiprocessing")
    
    print("PID of running process is : ",os.getpid())
    
    no = 5
    p1 = multiprocessing.Process(target=task1 , args = (no,))
    p2 = multiprocessing.Process(target = task2 , args = (no,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
if __name__ == "__main__":
    main()