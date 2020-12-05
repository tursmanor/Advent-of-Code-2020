from helpers import loadData

''' 
Starting at the top-left corner of your map and following a slope of right 3 
and down 1, how many trees would you encounter?
'''

data = loadData('day3-data.txt')

rowLen = len(data[0].strip())
horizPos = 0
horizMove = 3
treesHit = 0

# Skip the first line, since it doesn't matter
# Vert move is always one, so we don't account for it with a counter
for line in data[1:]:
    line = line.strip() # remove leading space
    curPos = (horizPos + horizMove) % rowLen
    
    if line[curPos] == '#':
        treesHit+=1

    horizPos = curPos

print("Number of trees hit: {}".format(treesHit))

'''
What do you get if you multiply together the number of trees 
encountered on each of the listed slopes?

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

'''

def calcTreesHit(data, horizMove, vertMove,rowLen):

    horizPos = 0
    vertPos = vertMove
    treesHit = 0

    for ind in range(len(data)):

        if (ind == vertPos):
            line = data[ind].strip()
            curPos = (horizPos + horizMove) % rowLen
    
            if line[curPos] == '#':
                treesHit+=1

            horizPos = curPos
            vertPos+=vertMove 
    
    return treesHit

run1 = calcTreesHit(data,1,1,rowLen)
run2 = calcTreesHit(data,3,1,rowLen)
run3 = calcTreesHit(data,5,1,rowLen)
run4 = calcTreesHit(data,7,1,rowLen)
run5 = calcTreesHit(data,1,2,rowLen)

print("Runs: {},{},{},{},{}".format(run1,run2,run3,run4,run5))
print("Multiplied output: {}".format(run1*run2*run3*run4*run5))

