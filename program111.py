
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    
    strn = ""
    for i in ch:
        i = ord(i)
        if i >= 65 and i <= 96:
            i += 32
        strn = strn + chr(i)
    
    return strn

def main():
    print("Enter input : ")
    char = input()

    value = Ascii(char)
    print(value)

if __name__ == "__main__":
    main()