from helpers import loadData
from itertools import chain

'''
How many bag colors can eventually contain at least one shiny gold 
bag? 
'''

data = loadData('day7-data.txt')

rules = {}
for line in data:
    [mainBag, innerBags] = line.split('contain')
    mainBag = mainBag[:-5].strip()
    
    # We can skip bags that contain nothing
    if 'no' in innerBags:
        continue 
    else:
        innerBags = innerBags[:-2].strip()  # remove newline and .
        bagsList = innerBags.split(', ')

        # Format into tuples of (number,color)
        numbers = []
        colors = []
        for bag in bagsList:
            words = bag.split(' ')
            numbers.append(int(words[0]))
            colors.append(' '.join(words[1:-1]))
        finalBags = zip(numbers,colors)

        rules[mainBag] = finalBags 

# Recursive function for appending valid bag colors onto an
# output list
def countBags(color,rules,out):
    tmp = []
    for key in rules:
        val = rules[key]
        for pair in val:
            if color in pair[1]:
                tmp.append(key)

    # Base case: no more bags that contain 'color' 
    if not tmp:
        return 
    else:
        out.append(tmp)
        for elem in tmp:
            countBags(elem,rules,out)

shinyBags = []
countBags('shiny gold',rules,shinyBags)

# Unnest the list of valid colors, then count unique values
allColors = list(chain(*shinyBags))
unique = set(allColors)
print("Valid number of colors: {}".format(len(unique)))

'''
How many individual bags are required inside your single shiny gold bag?
'''

def countInnerBags(color,rules):

    if color in rules:

        acc = 0
        colorsMults = rules[color]

        for indx in range(len(colorsMults)):
        
            curColor = colorsMults[indx][1]
            curMult = colorsMults[indx][0]
      
            acc += curMult + (curMult * countInnerBags(curColor,rules))

        return acc

    else: 
        # base case: empty bag
        return 0

    
a = countInnerBags('shiny gold',rules)
print("Number of nested bags: {}".format(a))