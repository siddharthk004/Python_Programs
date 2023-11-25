
def main():
    print("Enter first number: ")
    no1 = int(input())
    
    print("Enter second number: ")
    no2 = int(input())
    
    ans = 0
    
    try:
        ans = no1/no2
          
    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed",zobj)
        return 
    
    except Exception as zobj:
        print("Exception occures as ",zobj)
        return  
    
    finally:
        print("Thank you for using the application")    
    
    print("div is: ",ans)
    
if __name__ == "__main__":
    main()