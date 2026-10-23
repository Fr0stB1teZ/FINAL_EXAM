class Shaxs:
    def __init__(self, ism):
        self.ism = ism
        
class Talaba(Shaxs):
    pass

t = Talaba("Ali")
print(t.ism)
print(isinstance(t, Talaba))
print(isinstance(t, Shaxs))