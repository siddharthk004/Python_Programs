
def display(name,age,marks):
    print("name is: ",name)
    print("age is: ",age)
    print("marks are: ",marks)
    

def main():
    print("demonstration of keyword arguments ")
       
    display(name = "amit",age = 25,marks = 89)
    display(name = "sagar",age = 21,marks = 78)
    
if __name__ == "__main__":
    main()