
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    count = 0
    for i in ch:
        i = ord(i)
        if i >= 65 and i <= 96:
            count += 1
    return count
        
def main():
    print("Enter input : ")
    char = input()
    
    value = Ascii(char)
    
    print("Capital letter is : ",value)
        
if __name__ == "__main__":
    main()