
# sys package
import sys
    
def main():
    print("demonstration of command line arguments")
    
    print("number of command line arguments are: ",len(sys.argv))
    
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])
    ans = value1 + value2
    
    print("addition is : ",ans)
    
if __name__ == "__main__":
    main()