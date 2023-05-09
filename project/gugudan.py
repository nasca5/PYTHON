class GuGuDan : 
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    
    def mul(self) :
        result = self.first * self.second
        return result

GGD = GuGuDan(4,2)  

print(GGD.mul())

for i in range(1, 10) :
    print(f'{i:=^10}')
    print('')  
    for j in range(1, 10) :
        GGD = GuGuDan(i, j)
        print(f'{i} * {j} = {GGD.mul():<2}')
    print('')  
