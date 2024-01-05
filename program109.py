
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    for i in ch:
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            return True
    return False
        
def main():
    print("Enter input : ")
    char = input()
    
    value = Ascii(char)
    if value == True:
        print("Cointain vowels ")
    else:
        print("There is no vowels ")
        
if __name__ == "__main__":
    main()