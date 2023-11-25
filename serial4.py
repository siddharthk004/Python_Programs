
def square(no):
    return no * no;


def main():
    arr = [10,20,30,40,50]
    result = []
    
    for value in arr:
        ans = square(value)
        result.append(ans)
    
    print(result)
        
if __name__ == "__main__":
    main()

