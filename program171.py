
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def main():
    strs = ["flower","flow","flight"]
    
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    
    ans = ''
    
    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            break
        ans += first[i]
    
    print(ans)     
        

if __name__ == "__main__":
    main()