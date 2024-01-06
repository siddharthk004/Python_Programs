
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter Input : ")
    data = input()
    
    a,b,c,d = 0,0,0,0
    
    for i in range(len(data)):
        if data[i] == '(':
            a += 1
        elif data[i] == '{':
            b += 1
        elif data[i] == '[':
            c += 1
        elif data[i] == '<':
            d += 1
        
        if data[i] == ')':
            a -= 1
        elif data[i] == '}':
            b -= 1
        elif data[i] == ']':
            c -= 1
        elif data[i] == '>':
            d -= 1
            
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("True ")
    else:
        print("False")            
    
if __name__ == "__main__":
    main()