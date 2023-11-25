
# function defines another function that is inside it 
# and return as its return value

def marvellous(no1,no2):
    def add(A,B):   
        return A+B
    
    return add(no1,no2)        
def main():     
    ans = marvellous(10,7)
    print("addition is : ",ans)
    
    
if __name__ == "__main__":
    main() 