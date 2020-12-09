from helpers import loadData

'''
Run your copy of the boot code. Immediately before any instruction 
is executed a second time, what value is in the accumulator?
'''

data = loadData('day8-data.txt')

acc = 0
infLoop = False
curLine = 0
visitedIndices = [0]
while not infLoop:

    [rule,val] = data[curLine][:-1].strip().split(' ')
    sign = val[0]
    num = int(val[1:])
    
    if rule == 'acc':
        if sign == '+':
            acc += num 
        elif sign == '-':
            acc -= num 
        else:
            print("Acc value not formatted correctly.")
            break

        curLine += 1

    elif rule == 'jmp':
        if sign == '+':
            curLine += num
        elif sign == '-':
            curLine -= num
        else:
            print("Jmp value not formatted correctly.")
            break

    elif rule == 'nop':
        curLine += 1
        
    else:
        print("Error: unexpected input command {}".format(rule))
        break

    visitedIndices.append(curLine)

    if visitedIndices.count(curLine) > 1:
        infLoop = True

print('acc value before infinite loop: {}'.format(acc))   

'''
Fix the program so that it terminates normally by changing exactly one jmp (to nop) 
or nop (to jmp). What is the value of the accumulator after the program terminates?
'''

def testForInf(sequence):
    
    acc = 0
    infLoop = False
    curLine = 0
    visitedIndices = [0]
    goodSeqIndx = len(sequence) # zero indexed, so this is one after the final element
    
    while not infLoop:

        # We've made it past our known list data by one
        if curLine == goodSeqIndx:
            break

        [rule,val] = sequence[curLine][:-1].strip().split(' ')
        sign = val[0]
        num = int(val[1:])
    
        if rule == 'acc':
            if sign == '+':
                acc += num 
            elif sign == '-':
                acc -= num 
            else:
                print("Acc value not formatted correctly.")
                break

            curLine += 1

        elif rule == 'jmp':
            if sign == '+':
                curLine += num
            elif sign == '-':
                curLine -= num
            else:
                print("Jmp value not formatted correctly.")
                break

        elif rule == 'nop':
            curLine += 1
        
        else:
            print("Error: unexpected input command {}".format(rule))
            break

        visitedIndices.append(curLine)

        if visitedIndices.count(curLine) > 1:
            infLoop = True

    return acc, infLoop


# Iterate through the data trying swaps
for indx in range(len(data)):
    newData = data[:]
    [rule,val] = newData[indx][:-1].strip().split(' ')
    
    if rule == 'jmp':
        newData[indx] = newData[indx].replace('jmp','nop')
    elif rule == 'nop':
        newData[indx] = newData[indx].replace('nop','jmp')
    
    out = testForInf(newData)

    if out[1] == False:
        print("Line to modify: {}".format(indx))
        print("Acc value of new program: {}".format(out[0]))
        break


        
