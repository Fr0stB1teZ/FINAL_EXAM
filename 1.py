class Chiroq:
    def __init__(self):
        self.yoniq = False
        
    def yoq(self):
        self.yoniq = True
        
    def ochir(self):
        self.yoniq = False
        
    def holat(self):
        if self.yoniq:
            return "Yoniq"
        return "O'chiq"
    
c = Chiroq()
print(c.holat())
c.yoq()
print(c.holat())
c.ochir()
print(c.holat())