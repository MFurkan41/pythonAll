class Ogretmen():
    def __init__(self,ad,soyad,brans,maas):
        self.ad = ad
        self.soyad = soyad
        self.brans = brans
        self.maas = maas
    def bilgilerigoster(self):
        print("""
        ******************
        ÖĞRETMEN BİLGİLERİ
        ******************
        Ad : {}
        Soyad : {}
        Branş : {}
        Maaş : {}

        """.format(self.ad,self.soyad,self.brans,self.maas))
    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari
ogretmen1 = Ogretmen("Sultan","YOLAL","Coğrafya",1800)
ogretmen1.zam_yap(100)
ogretmen1.bilgilerigoster()
