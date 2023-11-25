

def main():
    print("enter number of elements that you want to store: ")
    length = int(input())
    
    arr = list()

    print("enter the elements: ")
    for i in range(length):
        value = int(input())
        arr.append(value)
    
    print("elements from the list are: ")
    for i in range(len(arr)):
        print(arr[i])
    
    
if __name__ == "__main__":
    main()