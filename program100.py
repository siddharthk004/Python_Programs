
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def ChkChar(ch):
    if ch == 'A' or ch == 'a':
        print(" Your exam at 7 AM ")
    if ch == 'B' or ch == 'b':
        print(" Your exam at 8:30 AM ")
    if ch == 'C' or ch == 'c':
        print(" Your exam at 9:20 AM ")
    if ch == 'D' or ch == 'd':
        print(" Your exam at 10:30 AM ")
            
def main():
    
    print("Enter Division : ")
    char = input() 
    
    if char == 'A' or char == 'B' or char == 'C' or char == 'D' or char == 'a' or char == 'b' or char == 'c' or char == 'd':
        ChkChar(char)
    else:
        print(" you've enter the wrong input ")
    
if __name__ == "__main__":
    main()