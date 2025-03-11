class AlisverisSepeti:
    def __init__(self):
        self.sepet = {}

    def urun_ekle(self, urun, miktar):
        if urun in self.sepet:
            self.sepet[urun] += miktar
        else:
            self.sepet[urun] = miktar
        print(f"{miktar} adet {urun} sepete eklendi.")

    def urun_cikar(self, urun, miktar):
        if urun in self.sepet:
            if self.sepet[urun] > miktar:
                self.sepet[urun] -= miktar
                print(f"{miktar} adet {urun} sepetten çıkarıldı.")
            else:
                del self.sepet[urun]
                print(f"{urun} tamamen sepetten çıkarıldı.")
        else:
            print(f"{urun} sepette bulunamadı.")

    def sepeti_goster(self):
        if not self.sepet:
            print("Sepetiniz boş.")
        else:
            print("\nSepetiniz:")
            for urun, miktar in self.sepet.items():
                print(f"- {urun}: {miktar} adet")

    def siparisi_tamamla(self):
        if not self.sepet:
            print("Sepetiniz boş! Sipariş verilemedi.")
        else:
            print("Siparişiniz tamamlandı! Sepetiniz sıfırlandı.")
            self.sepet.clear()


def menu():
    sepet = AlisverisSepeti()

    while True:
        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            urun = input("Eklemek istediğiniz ürün: ")
            miktar = int(input("Miktar: "))
            sepet.urun_ekle(urun, miktar)
        
        elif secim == "2":
            urun = input("Çıkarmak istediğiniz ürün: ")
            miktar = int(input("Miktar: "))
            sepet.urun_cikar(urun, miktar)
        
        elif secim == "3":
            sepet.sepeti_goster()  # Doğru şekilde çağrıldı
        
        elif secim == "4":
            sepet.siparisi_tamamla()
        
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

menu()