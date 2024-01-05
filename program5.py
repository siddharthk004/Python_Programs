
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 



def cheak(no):
        if no%5 == 0:
            return True
        else:
            return False

def main():
    value = 0
    print("Enter a number : ")
    num = int(input())
    
    ret = cheak(num)
    
    if ret == True:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
    
if __name__ == "__main__":
    main()