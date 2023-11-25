
# task = name of function
#elements = list of data elements

def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result = []
    for no in Elements:
        ret = Task(no)
        Result.append(ret)
    return Result

def ReduceX(Task,Elements):
    Result = 0
    for no in Elements:
        Result = Task(Result,no)
    return Result
