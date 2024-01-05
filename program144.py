
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = []
    temp1 = 0
    temp2 = 0
    temp3 = 0
    print("Enter Trade price for Six day : ")
    for i in range(6):
        print(i,": ",end="")
        list.append(int(input()))
        
    for x in range(5):
        for i in range(1,6,1):
            if list[x] > list[i]:    
                sum = list[x]-list[i]
                if sum > temp3:
                    temp1 = list[x]
                    temp2 = list[i]
                    temp3 = sum 
    print("buy on : ",temp1," Sell on : ",temp2," Profit is : ",temp3)
    
if __name__ == "__main__":
    main()