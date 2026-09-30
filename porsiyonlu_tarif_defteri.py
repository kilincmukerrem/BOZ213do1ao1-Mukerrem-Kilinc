
class Malzeme:
    def __init__(self, ad, miktar, birim):
        self.ad = ad
        self.miktar = miktar
        self.birim = birim

class Tarif:
    def __init__(self, isim, eski_porsiyon, malzemeler, yapilis):
        self.isim = isim
        self.eski_porsiyon = eski_porsiyon
        self.malzemeler = malzemeler
        self.yapilis = yapilis

    def porsiyonla(self, yeni_porsiyon):
        oran = yeni_porsiyon / self.eski_porsiyon
        print(f" {yeni_porsiyon} Kişilik {self.isim}")
        print("Malzemeleri:")
        for m in self.malzemeler:
            yeni_miktar = m.miktar * oran
            if isinstance(yeni_miktar, float) and yeni_miktar.is_integer():
                yeni_miktar = int(yeni_miktar)
            else:
                yeni_miktar = round(yeni_miktar, 2)
            print(f"- {yeni_miktar} {m.birim} {m.ad}")
        print(f"\nTarif:\n{self.yapilis}\n")



# TARİFLERİN EKLENECEĞİ YER
tarif_1 = Tarif(
    isim="Mini Cookieler",
    eski_porsiyon=16, 
    malzemeler=[
        Malzeme("Margarin veya Tereyağı", 100, "gram"), 
        Malzeme("Şeker", 0.5, "çay bardağı"), 
        Malzeme("Esmer Şeker", 0.5, "çay bardağı"), 
        Malzeme("Yumurta", 1, "adet"), 
        Malzeme("Vanilin", 1, "paket"), 
        Malzeme("Kabartma Tozu", 0.5, "paket"), 
        Malzeme("Un", 2, "su bardağı"), 
        Malzeme("Damla Çikolata", 1, "su bardağı") 
    ],
    yapilis="(Kısa Tarif) Malzemeleri karıştırıp hamur yoğurun, damla çikolataları ekleyin, minik toplar yapıp 15 dk pişirin."
)

tarif_2 = Tarif(
    isim="Pratik Elmalı Kurabiye",
    eski_porsiyon=10,     malzemeler=[
        # Hamur
        Malzeme("Tereyağı (Oda Isısında)", 150, "gram"), 
        Malzeme("Pudra Şekeri", 0.5, "su bardağı"), 
        Malzeme("Yumurta", 1, "adet"), 
        Malzeme("Kabartma Tozu", 1, "paket"), 
        Malzeme("Vanilya", 1, "paket"),
        Malzeme("Un", 3, "su bardağı"), 
        # İç Harcı
        Malzeme("Elma", 3, "adet"),
        Malzeme("Toz Şeker", 1, "yemek kaşığı"), 
        Malzeme("Tarçın", 1, "tatlı kaşığı"),
        Malzeme("Ceviz", 0.5, "çay bardağı"), 
        # Üzeri
        Malzeme("Pudra Şekeri (Üzeri için)", 1, "göz kararı") 
    ],
    yapilis="(Kısa Tarif) Elma, şeker, tarçın ve cevizi soteleyip soğutun. Hamur malzemelerini yoğurun. Hamura şekil verip harcı koyun, pişirin ve pudra şekeri serpin."
)

tarif_3 = Tarif(
    isim="Şekerpare",
    eski_porsiyon=6, 
    malzemeler=[
        # Hamur
        Malzeme("Tereyağı (Yumuşak)", 125, "gram"), 
        Malzeme("Sıvı Yağ", 0.5, "çay bardağı"), 
        Malzeme("Pudra Şekeri", 0.5, "su bardağı"), 
        Malzeme("Yumurta (1'inin sarısı üzeri için)", 2, "adet"),
        Malzeme("İrmik", 1, "çay bardağı"), 
        Malzeme("Vanilya", 1, "paket"), 
        Malzeme("Kabartma Tozu", 1, "paket"), 
        Malzeme("Un", 3, "su bardağı"), 
        # Şerbet
        Malzeme("Şeker", 3, "su bardağı"), 
        Malzeme("Su", 3, "su bardağı"),
        Malzeme("Limon", 0.25, "adet")
        ],
    yapilis="(Kısa Tarif) Şerbeti kaynatıp soğumaya bırakın. Hamuru yoğurup şekil verin, ayırdığınız yumurta sarısını sürüp pişirin. Sıcak tatlıya soğuk şerbet dökün."
)

tarif_4 = Tarif(
    isim="Krema Soslu Tava Böreği",
    eski_porsiyon=6, 
    malzemeler=[
        Malzeme("Yufka", 3, "adet"),
        # İç Harç
        Malzeme("Peynir", 1, "kase"), 
        Malzeme("Maydanoz", 1, "tutam"), 
        # Sos
        Malzeme("Süt", 1, "su bardağı"), 
        Malzeme("Krema", 100, "ml"), 
        Malzeme("Yumurta", 1, "adet"), 
        Malzeme("Sıvı Yağ", 0.25, "su bardağı") 
    ],
    yapilis="(Kısa Tarif) Sos malzemelerini çırpın. Tavaya yufkaları soslayarak kat kat dizin, araya peynirli harcı koyun. Tavada arkalı önlü pişirin."
)


sistemdeki_tarifler = [tarif_1, tarif_2, tarif_3, tarif_4]


# KULLANICI MENÜSÜ

while True:
    print("\n" + "="*30)
    print("1 - Tarif Listesini Görüntüle")
    print("2 - Porsiyon Hesabı Yap")
    print("3 - Çıkış")
    
    secim = input("Hangisini yapmak istersiniz? (1/2/3): ")

    if secim == '1':
        print("\nSİSTEMDEKİ TARİFLER:")
        for i, t in enumerate(sistemdeki_tarifler):
            print(f"{i+1}. {t.isim} ({t.eski_porsiyon} Kişilik)")

    elif secim == '2':
        aranan = input("\nPorsiyon hesabı yapmak istediğiniz tarifin adını yazın: ").lower()
        bulundu = False
        
        for t in sistemdeki_tarifler:
            if t.isim.lower() == aranan:
                bulundu = True
                try:
                    yeni_kisi_girdisi = input("Kaç kişilik olsun istiyorsunuz? (Örn: 0.5 veya 5): ").replace(',', '.')
                    yeni_kisi = float(yeni_kisi_girdisi)
                    t.porsiyonla(yeni_kisi)
                except ValueError:
                    print("Lütfen geçerli bir sayı giriniz.")
                break 
                
        if not bulundu:
            print("Bu isimde bir tarif bulunamadı. Listeden adına tam olarak bakabilirsiniz.")

    elif secim == '3':
        print("Program kapatılıyor...")
        break
    else:
        print("Hatalı tuşlama yaptınız.")
