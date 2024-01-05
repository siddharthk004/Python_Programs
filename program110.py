
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    strn = ""
    for i in ch:
        strn = i + strn
    return strn
        
def main():
    print("Enter input : ")
    char = input()
    
    value = Ascii(char)
    print(value)
        
if __name__ == "__main__":
    main()