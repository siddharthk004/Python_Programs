
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    count1 = 0
    count2 = 0
    
    for i in ch:
        i = ord(i)
        if i >= 97 and i <= 123:
            count1 += 1
            
        if i >= 65 and i <= 92:
            count2 += 1
            
    return count2-count1
        
def main():
    print("Enter input : ")
    char = input()
    
    value = Ascii(char)
    
    print("Difference is : ",value)
        
if __name__ == "__main__":
    main()