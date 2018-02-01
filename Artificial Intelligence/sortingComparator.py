from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        print(self.name,self.score)
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            nameObj = {a.name:-1,b.name:1}
            nameLst = sorted(nameObj.keys())
            return nameObj[nameLst[0]]
            
      
        
        

