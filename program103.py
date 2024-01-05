
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    ch = ord(ch)
    
    if ch >= 65 and ch <= 92:
        for i in range(ch,91):
            print(chr(i),end=" ")
        
    elif ch >= 97 and ch <= 124:
        for i in range(ch,123):
            print(chr(i),end=" ")
        
    else:
        pass
        
def main():
    print("Enter input : ")
    char = input()
    
    Ascii(char)
    
if __name__ == "__main__":
    main()