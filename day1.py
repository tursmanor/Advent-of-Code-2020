from helpers import loadData 

'''
Specifically, they need you to find the two entries that sum to 2020 and then 
multiply those two numbers together.
'''

data = loadData('day1-data.txt')
data = list(map(int,data))

for i in range(len(data)):
    for j in range(len(data)):
        if (i == j):
            continue
        if (data[i] + data[j] == 2020):
            print("{} + {} = 2020".format(data[i],data[j]))
            print("{} * {} = {}".format(data[i],data[j],data[i]*data[j]))

'''
They offer you a second one if you can find three numbers in your expense report 
that meet the same criteria.
'''

for i in range(len(data)):
    for j in range(len(data)):
        if (i == j):
            continue
        for k in range(len(data)):
            if (k == i or k == j):
                continue
            if (data[i] + data[j] + data[k] == 2020):
                print("{} + {} + {} = 2020".format(data[i],data[j],data[k]))
                print("{} * {} * {} = {}".format(data[i],data[j],data[k],data[i]*data[j]*data[k]))
