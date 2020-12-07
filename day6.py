from helpers import loadData

'''
For each group, count the number of questions to which anyone answered 
"yes". What is the sum of those counts?
'''

data = loadData('day6-data.txt')

# Separate the data into groups
groups = []
group = []
for elem in data:
    if elem == '\n':
        groups.append(group)
        group = []
    else:
        group.append(elem[:-1])
groups.append(group)

counts = []
for group in groups:
    curChars = []
    for person in group:
        curChars += list(person)
    counts.append(len(set(curChars)))

print("Sum of counts: {}".format(sum(counts)))

'''
For each group, count the number of questions to which everyone 
answered "yes". What is the sum of those counts?
'''
import functools

counts = []
for group in groups:
    curChars = []
    for person in group:
        curChars += list(person)
    
    overlap = []
    for char in curChars:
        if (curChars.count(char) == len(group)) and (char not in overlap):
            overlap.append(char)
    
    counts.append(len(overlap))

print("Sum of counts: {}".format(sum(counts)))        

