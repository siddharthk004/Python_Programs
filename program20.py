
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def CHKEqual(no1,no2,no3):
    if no1 == 0 | no2 == 0 | no3 == 0:
        return False
    else:
        sum = 1
        sum = no1*no2*no3
    return sum

def main():
    print("Please enter a three numbers : ")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
        
    bret = CHKEqual(num1,num2,num3)
    print("multiplication is : ",bret)

if __name__ == "__main__":
    main()