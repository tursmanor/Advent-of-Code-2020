from helpers import loadData

'''
The first step of attacking the weakness in the XMAS data is to find the first number 
in the list (after the preamble) which is not the sum of two of the 25 numbers before 
it. What is the first number that does not have this property?
'''

data = loadData('day9-data.txt')

def validSum(nums,x):
    # Check if x can be made of a sum of 2 unique elems in nums
    # Assumes numbers in output pair must be different

    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                continue
            
            if num1 + num2 == x:
                return True

    return False

preamble = 25
for indx in range(preamble,len(data)):

    prevValid = map(lambda x: int(x), data[indx-preamble:indx])
    curNum = int(data[indx])

    if not validSum(prevValid,curNum):
        print("Invalid number: {}".format(curNum))
        invalidNum = curNum

'''
[Y]ou must find a contiguous set of at least two numbers in your 
list which sum to the invalid number from step 1.

To find the encryption weakness, add together the smallest and 
largest number in this contiguous range; in this example, these 
are 15 and 47, producing 62.
'''

def sumContiguous(nums,x):

    for i in range(len(nums)):
        
        if i == x:
            continue

        curSet = [int(nums[i])]
        for j in range(i+1,len(nums)):
            
            if sum(curSet) == x:
                return curSet
            elif sum(curSet) > x:
                break
            else:
                curSet.append(int(nums[j]))
    return []

contig = sumContiguous(data,invalidNum)
print(contig)
print("Sum of {} and {}: {}".format(min(contig),max(contig),min(contig)+max(contig)))