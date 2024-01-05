
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    ch = ord(ch)
    
    if ch >= 65 and ch <= 92:
        ch += 32
        print(chr(ch))
        
    elif ch >= 97 and ch <= 124:
        ch -= 32
        print(chr(ch))
        
    else:
        print(chr(ch))
        
def main():
    print("Enter input : ")
    char = input()
    
    Ascii(char)
    
if __name__ == "__main__":
    main()