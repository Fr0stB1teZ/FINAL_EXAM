class Savat:
    def __init__(self):
        self.mahsulotlar = []
        
    def qosh(self, nomi):
        self.mahsulotlar.append(nomi)
        
    def __len__(self):
        return len(self.mahsulotlar)
    
    def __contains__(self, narsa):
        return narsa in self.mahsulotlar
        
s = Savat()
s.qosh("non")
s.qosh("sut")
print(len(s))
print("non" in s)
print("choy" in s)