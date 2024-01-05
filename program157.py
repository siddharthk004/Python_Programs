
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def merge(intervals):
    if not intervals:
        return []
    
    merged = []
    intervals.sort(key=lambda x: x[0])

    prev = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval
    
    merged.append(prev)
    return merged
    
def main():
    arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
   
    ans = merge(arr)
    print(ans)
    
if __name__ == "__main__":
    main()