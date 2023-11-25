batchname = ["PPA","MEAN","LB","LSP","PYTHON"]
batchfees = [18000,18300,18200,18050,18500]


for i in range(len(batchname)):
    print("batch name: ",batchname[i])
    print("batch fees: ",batchfees[i])
    print()
    
batches = {"PPA":18500,"python":18700,"LB":18000,"MEAN":18200}
print(batches) 

print(type(batches))

print(len(batches))

# print(batches("python"))

for value in batches:
    print(value)
    
for value in batches:
    print(batches[value])
    

for value in batches:
    print(value,batches[value])
    