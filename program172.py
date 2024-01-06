
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter Input : ")
    data = input()
    
    ans = ''
    flag = ''
    
    for i in range(len(data)):
        if i == 0:
            ans += data[i]
            flag = data[i]
        elif data[i] != flag:
            ans += data[i]
            flag = data[i]
        
    print(ans) 

if __name__ == "__main__":
    main()