import functools
def main():
    data = []
    print("enter the value you want to store: ")
    no = int(input())
    
    print("Enter value : ");
    for i in range(no):
        value = int(input())
        data.append(value)
        
    print("input data",data)
    moutput = functools.reduce(map((filter(lambda no : (no % 2 == 0),data))),filter(lambda no : (no % 2 == 0)))
    print(moutput)
if __name__ == "__main__":
    main()