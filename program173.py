
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter a input : ")
    data = input()
    
    for i in range(len(data)):
        if data[i].isalnum():
            x = data[i].lower()
            if x == 'a':
                print('2',end="")
            elif x == 'b':
                print('22',end="")
            elif x == 'c':
                print('222',end="")
            elif x == 'd':
                print('3',end="")
            elif x == 'e':
                print('33',end="")
            elif x == 'f':
                print('333',end="")
            elif x == 'g':
                print('4',end="")
            elif x == 'h':
                print('44',end="")
            elif x == 'i':
                print('444',end="")
            elif x == 'j':
                print('5',end="")
            elif x == 'k':
                print('55',end="")
            elif x == 'l':
                print('555',end="")
            elif x == 'm':
                print('6',end="")
            elif x == 'n':
                print('66',end="")
            elif x == 'o':
                print('666',end="")
            elif x == 'p':
                print('7',end="")
            elif x == 'q':
                print('77',end="")
            elif x == 'r':
                print('777',end="")
            elif x == 's':
                print('7777',end="")
            elif x == 't':
                print('8',end="")
            elif x == 'u':
                print('88',end="")
            elif x == 'v':
                print('888',end="")
            elif x == 'w':
                print('9',end="")
            elif x == 'x':
                print('99',end="")
            elif x == 'y':
                print('999',end="")
            elif x == 'z':
                print('9999',end="")
        
    
if __name__ == "__main__":
    main()