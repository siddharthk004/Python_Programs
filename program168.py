
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter Input : ")
    data = input()
    demo = ""
    
    for x in data:
        if x.isalnum():
            x = x.lower()
            demo += x
    
    solution = demo[::-1]
    
    flag = False
    
    for i in range(len(demo)):
        if demo[i] != solution[i]:
            flag = True
    
    if flag == True:
        print("Not palindrome")
    else:
        print("Palindrome")
    
if __name__ == "__main__":
    main()
    