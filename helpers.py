def loadData(filename):
    data = []

    with open(filename,mode='r') as dataFile:
        for cur in dataFile:
            data.append(cur)
    
    return data
