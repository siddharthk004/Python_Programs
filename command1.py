
# sys package
import sys
    
def main():
    print("demonstration of command line arguments")
    
    print("number of command line arguments are: ",len(sys.argv))
    
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    
if __name__ == "__main__":
    main()