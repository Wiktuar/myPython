def inputData():
    inputData = input().split(" ")
    return inputData

def writeInBook1(inputData):
    return inputData    

def writeInBook2(inputData):
    inputData = map(lambda x: x + ', ', inputData)
    finalStr = ""
    for data in inputData:
        finalStr += data
    return finalStr[:len(finalStr) - 2]
