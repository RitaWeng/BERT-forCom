import sys
from collections import Counter

s = sys.stdin.readlines()

longInput = s[0].strip()
splitsymbol = s[1].strip()

def findOneOfMax(inputDic):
    max_count=0
    max_num=''
    # output_key_value_list=[]
    for num, count in inputDic.items():
        if (max_count < count):
            max_count = count
            #max_num = num
    for element, counts in inputDic.items():
        if (counts==max_count):
            # output_key_value_list.append(element)
            print(element)
    # return(output_key_value_list)

d = Counter(longInput.split(splitsymbol))

findOneOfMax(d)