
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    ch = ord(ch)
    print("Decimal : ",ch)
    print("Octal : ",oct(ch))
    print("HexaDecimal : ",hex(ch))
    
        
def main():
    print("Enter input : ")
    char = input()
    
    Ascii(char)
        
if __name__ == "__main__":
    main()