
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def CHKGreater(no1):
    if no1 > 100:
        return True
    else:
        return False


def main():
    print("Please enter a number : ")
    num = int(input())
    
    bret = CHKGreater(num)
    if bret == True:
        print(" Greater ")
    else:
        print(" Smaller ")

if __name__ == "__main__":
    main()