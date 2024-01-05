
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def percentage(no1,no2):
    if no1 < no2:
        return 0;
    else:
        return no2/no1*100

def main():
    print("Enter Total Marks : ")
    num1 = int(input())
    
    print("Enter Obtained Marks : ")
    num2 = int(input())
        
    bret = percentage(num1,num2)
    print("percentage is : ",bret,"%")

if __name__ == "__main__":
    main()