
def display(name,age,marks = 90):
    print("name is: ",name)
    print("age is: ",age)
    print("marks are: ",marks)
    

def main():
    print("demonstration of default arguments ")
    display("amit",23)
    display("sagar",22,78)
     
if __name__ == "__main__":
    main()