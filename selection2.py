
def chkevenodd(value):
    result = value % 2
    
    if(result == 0):
        print("number is even")
    else:
        print("number is odd")
    

def main():
    
    print("enter number: ")
    no = int(input())
    
    chkevenodd(no)
    
if __name__ == "__main__":   # starter
    main()     # function call