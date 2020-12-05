from helpers import loadData

'''
Each line gives the password policy and then the password. The password policy indicates 
the lowest and highest number of times a given letter must appear for the password to 
be valid. For example, 1-3 a means that the password must contain a at least 1 time and
at most 3 times.

How many passwords are valid according to their policies?
'''

data = loadData('day2-data.txt')

numValid = 0

for line in data:
    [rule,pwd] = line.split(':')
    [count,letter] = rule.split(' ')
    [minNum,maxNum] = count.split('-')

    countLetter = len(filter(lambda x: x == letter , pwd))
    
    if (countLetter <= int(maxNum)) and (countLetter >= int(minNum)):
        numValid+=1

print("Number of valid passwords: {}".format(numValid))

'''
Each policy actually describes two positions in the password, where 1 means the first 
character, 2 means the second character, and so on. (Be careful; Toboggan Corporate 
Policies have no concept of "index zero"!) Exactly one of these positions must contain 
the given letter. Other occurrences of the letter are irrelevant for the purposes of 
policy enforcement.
'''

def testCompliance(string,indices,letter):

    value1 = string[indices[0]-1] == letter
    value2 = string[indices[1]-1] == letter

    # ^ is the equivalent to XOR
    if (value1 ^ value2):
        return True
    else:
        return False


numValid = 0

for line in data:
    [rule,pwd] = line.split(':')
    [inds,letter] = rule.split(' ')
    [indx1,indx2] = inds.split('-')

    isValid = testCompliance(pwd.strip(),[int(indx1),int(indx2)],letter)
    
    if isValid:
        numValid+=1

print("Number of valid passwords: {}".format(numValid))