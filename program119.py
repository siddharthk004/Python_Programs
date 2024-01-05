
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch,chrX):
    count = 0
    value = 0
    flag = False
    
    for i in ch:
        count += 1
        if i == chrX:
            flag = True
            value = count
        
    if flag == False:
        value = -1
        return value
    else:
        return value
    
def main():
    
    print("Enter input : ")
    char = input()
    
    print("Enter character : ")
    charX = input()

    value = Ascii(char,charX)
    print(value)
    
if __name__ == "__main__":
    main()