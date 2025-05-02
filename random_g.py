import math
import random

mGroup = int(input('Number of people per group: '))
class Group():
    def __init__(self, myList, m):
        self.myList = myList
        self.m = m
        self.nGroups = math.ceil(len(myList)/self.m)
    
    def generateGroups(self):
        group = []
        list_group = []
        visited_names = []
        #self.shuffle(self.myList)

        leftover = self.myList[-(len(self.myList) % self.m) - self.m:]
        groupable = self.myList[:-(len(self.myList) % self.m) - self.m]
        if groupable == []:
            groupable = self.myList[:-(len(self.myList) % self.m)]
            leftover = self.myList[-(len(self.myList) % self.m):]


        if self.m == len(groupable):
            list_group.append(groupable)
            #return list_group
            
        else:
            for i in range(0, len(groupable) + 1):
                if len(group) < self.m:
                    group.append(groupable[i])
                    
                else:
                    list_group.append(group)
                    group = []
                    if i < len(groupable):
                        group.append(groupable[i])
            
        nLeftOvers = self.nGroups - len(list_group)
        mLeftOvers = math.floor(len(leftover)/nLeftOvers)

        for i in range(0, len(leftover) + 1):
            if len(group) < mLeftOvers:
                group.append(leftover[i])
                
            else:
                if i == len(leftover) - 1:    
                    group.append(leftover[-1])
                    list_group.append(group)
                    return list_group
                list_group.append(group)
                group = []
                if i < len(leftover):
                    group.append(leftover[i])

        

        return list_group


    def shuffle(self, list):
        random.shuffle(list)
        


myInput = [
    'asdf', 'qwerasdf', 'qwedfasdfzx', 'jklñ', 'qwer', 'poiuio', 'mnbvbn', 
    'asdfasdfjkjk', 'asdfyuioqwier', 'Reaul', 'asdfjqyqdjxk', 'element12', 
    'element13', 'element14', 'element15', 'element16', 'element17', 
    'element18', 'element19', 'element20', 'element21', 'element22', 
    'element23', 'element24', 'element25', 'element26', 'element27', 
    'element28', 'element29', 'element30'
]
group = Group(myInput, mGroup)
print(f'Number of groups: {group.nGroups}')
for i in group.generateGroups():
    print(i)
