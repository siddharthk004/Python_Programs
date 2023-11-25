import os.path

def main():
    print("Enter the name of file that you want to open for Writting purpose : ")
    File_name = input()
    
    if os.path.exists(File_name):
        fobj = open(File_name,"a")    # append mode
        if fobj:
            print("data successfully open for writing")
            print("Enter the data that you want to write in file : ")
            data = input()
            
            fobj.write(data)   # write the data into the file
            
            fobj.close()
        else:
            print("Unable to write data")  
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()