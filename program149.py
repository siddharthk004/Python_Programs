
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def productExceptSelf(nums):
    product, zero_cnt = 1, 0
    for num in nums:
        if num != 0:
            product *= num
        else:
            zero_cnt += 1
    
    if zero_cnt > 1:
        return [0]*len(nums)
    
    if zero_cnt != 0:
        return [0 if num != 0 else int(product) for num in nums] 
    else:
        return [int(product/num) if num != 0 else product for num in nums]

def main():
    my_list = [1,2,3,4]
    
    ans = productExceptSelf(my_list)
    print(ans)
    
if __name__ == "__main__":
    main()
