
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch,chrX):
    
    for i in ch:
        if i == chrX:
            return True
    return False
    
def main():
    
    print("Enter input : ")
    char = input()
    
    print("Enter character : ")
    charX = input()

    value = Ascii(char,charX)
    
    if value == True:
        print(" present ")
    else:
        print(" not present ")

if __name__ == "__main__":
    main()