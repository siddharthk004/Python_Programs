
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Ascii(ch):
    count = 0
    for i in ch:
        if i == " ":
            count += 1
    return count
    
def main():
    print("Enter input : ")
    char = input()

    value = Ascii(char)
    
    print(value)

if __name__ == "__main__":
    main()