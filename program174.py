
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    print("Enter a input : ")
    data = input()

    dict = {}

    for i in range(len(data)):
        if data[i] in dict:
            dict[data[i]] += 1
        else:
            dict[data[i]] = 1
            
    for it,it2 in dict.items():
        if it2 > 1:
            print(str(it)," count is : ",str(it2)) 
    

if __name__ == "__main__":
    main()