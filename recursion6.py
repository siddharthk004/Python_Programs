i = 0

def display():
    global i
    print("Inside display : ",i)
    i+=1
    display()

def main():
    display()

if __name__ == "__main__":
    main()