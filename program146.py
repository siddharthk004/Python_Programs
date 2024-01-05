
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 


def main():
    list = [1,2,3,2,4,3,5,6,7,7,3,1]
    arr = []
    for i in range(len(list)-1):
        for j in range(i+1,len(list),1):
            if list[i] == list[j]:
                if list[i] not in arr:
                    arr.append(list[i])
        
    print(list)
    print("\n\n")
    print(arr)

if __name__ == "__main__":
    main()