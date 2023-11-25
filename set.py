
set1 = {11,"hello",90.78,False,12,54}
print(set1)

# print(set1[2])

for value in set1:
    print(value)
    
set2 = {11,21,53,43,11}
print(set2)

# set2[2] = 25
set2.add(101)
print(set2)

set2.discard(101)
print(set2)

for value in set2:
    if(11 == value):
        print("element is present")
        break
    
# 
