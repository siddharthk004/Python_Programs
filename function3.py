
# function accept more parameter and return nothing
def marvellous(Name,age,city):
    print("Inside Marvellous Function")
    print("Welcome : ",Name)
    print("your age is : ",age)
    print("your city is : ",city)

def main():
    marvellous("Siddharth",28,"Newasa")
    marvellous(Name="Siddharth",age = 28,city= "Newasa")
    
if __name__ == "__main__":
    main()