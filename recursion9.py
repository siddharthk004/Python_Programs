import sys

def display(i):
    if(i < 6):
        print(i)
        i+=1
        display(i)

def main():
    display(1)
    
if __name__ == "__main__":
    main()