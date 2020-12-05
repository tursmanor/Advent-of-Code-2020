from helpers import loadData

'''
Every seat also has a unique seat ID: multiply the row by 8, then add the column. 

As a sanity check, look through your list of boarding passes. What is the highest 
seat ID on a boarding pass?

Total rows: 128 (0-127)
Total cols: 8 (0-7)
'''

data = loadData('day5-data.txt')

def getSeatID(row,col):
    return (row * 8) + col

def calcRow(rows):
    # F = '0', B = '1'
    number = ''
    for char in rows:
        if char == 'F':
            number += '0'
        else:
            number += '1'
    
    return int(number,2)

def calcCol(cols):
    # L = '0', R = '1'
    number = ''
    for char in cols:
        if char == 'L':
            number += '0'
        else:
            number += '1'
    
    return int(number,2)

seatIDs = []
for seat in data:
    seat = seat.strip().split('/n')[0]
    
    rows = []
    cols = []
    for char in seat:
        if char in ['F','B']:
            rows.append(char)
        else:
            cols.append(char)
    
    curID = getSeatID(calcRow(rows),calcCol(cols))
    seatIDs.append(curID)

print("Highest ID: {}".format(max(seatIDs)))

'''
Your seat wasn't at the very front or back, though; the seats with IDs +1 
and -1 from yours will be in your list.

What is the ID of your seat?
'''

seatIDs.sort()

prev = seatIDs[0]
gaps = []
for seat in seatIDs[1:]:
    if (prev + 1 != seat):  # Gap detected
        gaps.append(prev+1)
    prev = seat

print(gaps) # only one for my dataset, so no need to check for the +1 case
