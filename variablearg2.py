
def display(*values):
    for i in range(len(values)):
        print(values[i])
        
def main():
    print("demonstration of variablle number of arguments ")
    
    display(10,20,30,40,50,60)
    display(11,21,31,41) 
    
if __name__ == "__main__":
    main()