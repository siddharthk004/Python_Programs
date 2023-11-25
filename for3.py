# demonstration of range function
# range(start, end, step)
# start : optional
# end : explictely provided by the programmer
# step : optional


def main():
    sum = 0
    for i in range(5,25,5):    
        sum +=i
        print(sum)
        
if __name__ == "__main__":   # starter
    main()     # function call