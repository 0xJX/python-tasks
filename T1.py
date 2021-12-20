
def GetNumberList():
    validNumbers = []
    for i in range(2000, 3200):
        if(i % 5 == 0):
            print(f'Number {i} was divisible with 5, continue.')
            continue
        if(i % 7 == 0):
            print(f'Number {i} was divisible with 7, added to list!')
            validNumbers.append(i)
    return validNumbers

print("\nPrinting the list:")

populatedList = GetNumberList()
for idx, num in enumerate(populatedList, start=1):
    print(f'{idx}/{len(populatedList)} = {num}')
