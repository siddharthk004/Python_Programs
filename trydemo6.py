
def main():
    try:
            
        print("Enter first number: ")
        no1 = int(input())
        
        print("Enter second number: ")
        no2 = int(input())
        
        ans = 0
        
        ans = no1/no2
             
    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed",zobj)
        return 
    
    except Exception as zobj:
        print("Exception occures as ",zobj)
        return      
    
    print("div is: ",ans)
    
if __name__ == "__main__":
    main()