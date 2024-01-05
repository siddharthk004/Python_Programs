
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    ch = ord(ch)
    
    if ch >= 65 and ch <= 92:
        return False
    
    elif ch >= 97 and ch <= 124:
        return False
    
    elif ch >= 48 and ch <= 57:
        return False
        
    else:
        return True
        
def main():
    print("Enter input : ")
    char = input()
    
    flag = Ascii(char)
    
    if flag == True:
        print("It is special character")
    else:
        print("It is not special character")
        
if __name__ == "__main__":
    main()