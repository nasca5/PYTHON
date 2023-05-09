
# make gugu by class
class GuGuDan : 
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    
    def mul(self) :
        result = self.first * self.second
        return result

# make gugu by def
def gugu(num) :
    result = []
    for i in range(1, 10) :
        result.append(num * i)
    return result

GGD = GuGuDan(4,2)  

for i in range(1, 10) :
    print(f'{i:=^10}')
    print('')  
    for j in range(1, 10) :
        GGD = GuGuDan(i, j)
        print(f'{i} * {j} = {GGD.mul():<2}')
    print('')  

for i in range(1, 10) :
    result = gugu(i)
    print(f'{i:=^10}')
    print('')
    for j in range(0, 9) :
        print(f'{i} * {j + 1} = {result[j]}')
    print('')
