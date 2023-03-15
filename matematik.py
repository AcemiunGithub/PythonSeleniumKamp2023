class Matematik:

    #class çağırırken parantez aç kapa yapınca bu alttaki fonsiyon otomotik çalışıyor
    #super base klası demek initialize başlangıç demek
    def __init__(self,a,b):#constructor-yapıcı blok
        self.sayi1=a
        self.sayi2=b
        print("Matematik başladı referans oluşuruldu")

    def topla(self):
        return self.sayi1+self.sayi2
    def cikar(self):
        return self.sayi1-self.sayi2
    def bol(self):
        return self.sayi1/self.sayi2
    def carp(self):
        return self.sayi1*self.sayi2

matematik=Matematik(14,7)
sonuc1=matematik.bol()
sonuc2=matematik.cikar()
print("sonuç:"+str(sonuc1))
print("sonuç:"+str(sonuc2))

#inheritance
class Istatistik(Matematik):
    def __init__(self, a, b):
        super().__init__(a, b)
    def varyansHesap(self):
        return self.sayi1*self.sayi2

istatistik=Istatistik(8,9)
print("Varyans:"+str(istatistik.varyansHesap()))
        
