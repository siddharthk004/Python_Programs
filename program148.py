
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    list1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    list2 = list1[::-1]
    
    list3,list4,MaxL,MaxR,sub,ans = [0],[0],0,0,0,0
    
    for i in range(len(list1)-1):
        if list1[i] > MaxL:
            MaxL = list1[i]
        list3.append(MaxL)
            
        if list2[i] > MaxR:
            MaxR = list2[i]
        list4.append(MaxR)
    
    list4 = list4[::-1]
    
    for i in range(len(list1)):
        sub = list3[i] - list4[i]
        if sub < 0:
            sub = -(sub)
        ans += int(list1[i] - int(sub))
    if ans < 0:
        ans = -(ans)
        
    print(ans)

if __name__ == "__main__":
    main()
    