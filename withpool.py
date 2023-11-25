import multiprocessing

def square(no):
    return no * no;


def main():
    arr = [10,20,30,40,50]
    Result = []
    
    p = multiprocessing.Pool()
    Result = p.map(square,arr)
    p.close()
    p.join()
    
    print(Result)
        
if __name__ == "__main__":
    main()

