
subTotal = 66
personDict = {'Name1': 19, 'Name2': 14, 'Name3': 9, 'Name4': 9, 'Name5': 15}
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

