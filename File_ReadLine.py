import os.path
# demonstration of file handling
def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")    # read mode
        if fobj:
            print("data successfully open for reading")
            Line1 = fobj.readline()
            Line2 = fobj.readline()
            Line3 = fobj.readline()
            print("first line is : ",Line1)
            print("second line is : ",Line2)
            print("third line is : ",Line3)
                       
            fobj.close()
        else:
            print("Unable to open data")  
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()