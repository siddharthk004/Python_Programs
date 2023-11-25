
def Addition(no1,no2):
    result = 0
    result = no1 + no2
    return result


def main():
    value1 = int(input("enter first number: "))
    value2 = int(input("enter second number: "))

    answer = 0

    answer = Addition(value1,value2)
    print("result is: ",answer)
    