
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch,chrX):
    count = 0
    flag = False
    for i in ch:
        count += 1
        if i == chrX:
            flag = True
            return count
    if flag == False:
        count = -1
        return count
    
def main():
    
    print("Enter input : ")
    char = input()
    
    print("Enter character : ")
    charX = input()

    value = Ascii(char,charX)
    print(value)
    
if __name__ == "__main__":
    main()