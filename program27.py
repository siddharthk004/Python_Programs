
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def number(no1):
    if no1 < 50:
        print("-- Small --")
    elif no1 > 50 and no1 < 100:
        print("-- Medium --")
    elif no1 > 100:
        print("-- Large --")
    else:
        print("didn`t Recognize")
    
def main():
    print("Enter a number : ")
    num = int(input())
    
    number(num)

if __name__ == "__main__":
    main()