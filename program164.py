
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter String : ")
    string = input()
    
    newstr = ""
    
    for s in string:
        if s.isalnum():
            newstr += s
            
    if newstr == newstr[::-1]:
        print("It is palindrome")
    else:
        print("It is not palindrome")
    
if __name__ == "__main__":
    main()
    