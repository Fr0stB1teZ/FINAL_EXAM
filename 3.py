class Shaxs:
    def __init__(self):
        self.__ism = "Noma'lum"
        
    def ismni_ber(self, ism):
        if not ism:
            print("Ism bo'sh bo'lishi mumkin emas")
        else:
            self.__ism = ism
            
    def ismni_ol(self):
        return self.__ism
    
s = Shaxs()
print(s.ismni_ol())
s.ismni_ber("Ali")
s.ismni_ber("")
print(s.ismni_ol())