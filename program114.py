
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
        
        if i >= 97 and i <= 124:
            pass
        elif i >= 65 and i <= 92:
            pass
        else:
            print(chr(i),end="")
            

def main():
    print("Enter input : ")
    char = input()

    Ascii(char)

if __name__ == "__main__":
    main()