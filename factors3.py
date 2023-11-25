def main():
    no = 0
    print("enter number: ")
    no = int(input())
    displayfactors(no)

def displayfactors(value):
    for i in range(1,value,1):
        if(value % i == 0):
            print(i)


if __name__ == "__main__":
    main()