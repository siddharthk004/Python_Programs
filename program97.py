
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def ChkChar(ch):
    if ch >= 'A' and ch <= 'Z':
        return True
    else:
        return False
            
def main():
    
    print("Enter input  : ")
    char = input() 
    
    flag = ChkChar(char)
    
    if flag == True:
        print(" It is Capital letter ")
    else:
        print(" It is not Capital letter ")
    
if __name__ == "__main__":
    main()