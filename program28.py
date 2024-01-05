
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def number(no1):
    if no1 == 0:
        print("-- Zero --")
    elif no1 == 1:
        print("-- One --")
    elif no1 == 2:
        print("-- Two --")
    elif no1 == 3:
        print("-- Three --")
    elif no1 == 4:
        print("-- Four --")
    elif no1 == 5:
        print("-- Five --")
    elif no1 == 6:
        print("-- Six --")
    elif no1 == 7:
        print("-- Seven --")
    elif no1 == 8:
        print("-- Eight --")
    elif no1 == 9:
        print("-- Nine --")
    elif no1 == 10:
        print("-- Ten --")
    
def main():
    print("Enter a number : ")
    num = int(input())
    
    if num > 0 and num < 10:
        number(num)
    else:
        print("Wrong number")

if __name__ == "__main__":
    main()