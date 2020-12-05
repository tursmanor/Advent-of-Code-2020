from helpers import loadData

'''
The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Count the number of valid passports - those that have all required fields. Treat cid 
as optional. In your batch file, how many passports are valid?
'''

data = loadData('day4-data.txt')

# Make a list of dictionaries, where each dict is a passport entry
groupedData = []
curPassport = {}
for line in data:
    if (line == '\n'):
        groupedData.append(curPassport)
        curPassport = {}
    else:
        pairs = line.split(' ')
        for p in pairs:
            [label,data] = p.split(':')
            curPassport[label] = data.strip().split('/n')[0]

# Fit in final entry that is not followed by a newline
groupedData.append(curPassport)

# Count number of valid passports
validPass = 0 
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for passport in groupedData:
    numGoodFields = 0
    for f in fields:
        if f in passport:
            numGoodFields+=1
    
    if (numGoodFields == len(fields)):
        validPass +=1
    
print("Number of valid passports: {}".format(validPass))
    
'''
You can continue to ignore the cid field, but each other field has strict rules about 
what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

'''

def checkPassport(passport):
    # BYR
    byr = int(passport['byr'])
    if (byr < 1920) or (byr > 2002):
        return False

    # IYR
    iyr = int(passport['iyr'])
    if (iyr < 2010) or (iyr > 2020):
        return False 

    # EYR
    eyr = int(passport['eyr'])
    if (eyr < 2020) or (eyr > 2030):
        return False

    # HGT
    hgt = passport['hgt']
    unit = hgt[-2:]
    value = int(hgt[:-2])
    if unit == 'cm':
        if (value < 150) or (value > 193):
            return False
    elif unit == 'in':
        if (value < 59) or (value > 76):
            return False 
    else:
        return False
    
    # HCL
    hcl = passport['hcl']
    validChar = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    if (hcl[0] != '#'):
        return False
    else:
        if len(hcl) != 7:
            return False
        else:
            for elem in hcl[1:]:
                if elem not in validChar:
                    return False

    # ECL
    ecl = passport['ecl']
    validECL = ['amb','blu','brn','gry','grn','hzl','oth']
    if len(ecl) != 3:
        return False
    else:
        if ecl not in validECL:
            return False  

    # PID
    pid = passport['pid']
    validPID = ['0','1','2','3','4','5','6','7','8','9']
    if len(pid) != 9:
        return False 
    else:
        for char in pid:
            if char not in validPID:
                return False
    
    # If we've made it this far.....
    return True

# Count number of valid passports
validPass = 0 
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for passport in groupedData:
    numGoodFields = 0
    for f in fields:
        if f in passport:
            numGoodFields+=1
    
    if (numGoodFields == len(fields)) and checkPassport(passport):
        validPass +=1
    
print("Number of valid passports: {}".format(validPass))