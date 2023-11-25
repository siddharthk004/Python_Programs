import multiprocessing
import os

def task1():
    print("Executing the firsgt task...")
    print("PID of running process for task 1 : ",os.getpid())
    
def task2():
    print("Executing the second task...")
    print("PID of running process for task 2: ",os.getpid())
      
def main():
    print("demonstration of multiprocessing")
    
    print("PID of running process is : ",os.getpid())
    task1()
    task2()

    
if __name__ == "__main__":
    main()