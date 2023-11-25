
def displayfactors(value):
    i = 1
    while(i < value):
        if(value % i == 0):
            print(i)
        i = i + 1

def main():
    no = 0
    print("enter number: ")
    no = int(input())
    displayfactors(no)


if __name__ == "__main__":
    main()