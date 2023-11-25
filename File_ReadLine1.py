import os.path
# demonstration of file handling
def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"r")    # read mode
        if fobj:
            print("data successfully open for reading")
            print("Data from file is ")
            for line in fobj:
                print(line)
                
            fobj.close()
        else:
            print("Unable to open data")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()