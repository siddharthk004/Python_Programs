
def display(*values):
    print(type(values))
    print(len(values))
    print(values)
    
def main():
    print("demonstration of variablle number of arguments ")
    
    display(10,20,30,40,50,60) 
if __name__ == "__main__":
    main()