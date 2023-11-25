
def main():
    print("enter number: ")
    no = int(input())
    
    result = no % 2
    
    if(result == 0):
        print("number is even")
    else:
        print("number is odd")
    
if __name__ == "__main__":   # starter
    main()     # function call