# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

subTotal = 66
personDict = {'Carson': 19, 'Sean': 14, 'Bijan': 9, 'Wray': 9, 'Ben': 15}
def percentPer(subTotal, personDict):
    res = []
    for person in personDict.values():
        feeShare = ((person/subTotal))
        res.append(feeShare)
    return res
resList=percentPer(subTotal,personDict)
fees = 19
def totalFeeShare(fees,resList):
    totalPerPersonFee = []
    for i in resList:
        percentFee = (fees*i)
        totalPerPersonFee.append(percentFee)
    print(totalPerPersonFee)
    print(type(totalPerPersonFee))
    return totalPerPersonFee
feeTotal = totalFeeShare(fees,resList)
subFinal = personDict.values()
subtotalList= list(subFinal)
print(subtotalList)
print(type(subtotalList))
finalList = [subtotalList[i] + feeTotal[i] for i in range(len(subtotalList))]
print(finalList)

