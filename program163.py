
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    arr  = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    query = [[0, 4],[1, 3],[2, 4]] 
    
    for q in query: 
        L,R = q
        s = 0
        for i in range(L,R+1):
            s += arr[i]
        print("Sum of",q,"is",s)
            
if __name__ == "__main__":
    main()