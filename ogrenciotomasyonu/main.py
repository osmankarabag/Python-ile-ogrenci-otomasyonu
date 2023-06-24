import csv

ogrenciler = []
def ogrencileri_yukle():
    try:
        with open('ogrenciler.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ogrenciler.append(row)
    except Exception as e:
        print("Öğrenciler yüklenirken bir hata oluştu:", str(e))
    return ogrenciler
def ogrencileri_kaydet(ogrenciler):
    try:
        with open('ogrenciler.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in ogrenciler:
                writer.writerow(row)
    except Exception as e:
        print("Öğrenciler kaydedilirken bir hata oluştu:", str(e))


def ogrenci_ekle():
    try:
        while True:
            ad = input("Adı: ")
            if ad.isalpha():
                break
            else:
                print("Hatalı giriş! Ad sadece harflerden oluşmalıdır. Tekrar deneyin.")

        while True:
            soyad = input("Soyadı: ")
            if soyad.isalpha():
                break
            else:
                print("Hatalı giriş! Soyad sadece harflerden oluşmalıdır. Tekrar deneyin.")

        while True:
            yaş = input("Yaşı: ")
            if yaş.isdigit():
                break
            else:
                print("Hatalı giriş! Yaş sadece sayılardan oluşmalıdır. Tekrar deneyin.")
        while True:
            kredi = input("Kredisi: ")
            if kredi.isdigit():
                break
            else:
                print("Hatalı giriş! Kredi sadece sayılardan oluşmalıdır. Tekrar deneyin.")


        yeni_ogrenci = [ad, soyad, yaş,kredi]
        ogrenciler.append(yeni_ogrenci)
        ogrencileri_kaydet(ogrenciler)
        print("Öğrenci eklendi.")

        devam = input("Devam etmek için 'E'ye, ana menüye dönmek için 'H'ye basın: ")
        if devam.upper() == "E":
            ogrenci_ekle()  # Yeni bir öğrenci eklemek için fonksiyonu tekrar çağır
        elif devam.upper() == "H":
            return  # Ana menüye dön
        else:
            print("Hatalı giriş! Geçerli bir seçim yapın.")
    except Exception as e:
        print("Öğrenci eklenirken bir hata oluştu:", str(e))



def ogrenci_guncelle():
    try:
        while True:
            ad = input("Güncellenecek öğrencinin adını girin (0: Ana Menü): ")
            if ad == "0":
                return  # Ana menüye dön
            bulundu = False
            for ogrenci in ogrenciler:
                if ogrenci[0] == ad:
                    print("Öğrenci bilgileri:")
                    print("Adı: ", ogrenci[0])
                    print("Soyadı: ", ogrenci[1])
                    print("Yaşı: ", ogrenci[2])
                    print("Kredisi: ", ogrenci[3])

                while True:
                    secim = input("Hangi bilgiyi güncellemek istiyorsunuz?\n1. Soyadı\n2. Yaşı\n3. Kredisi\n Seçiminizi yapın (1-3): ")
                    if secim.isdigit() and 1 <= int(secim) <= 5:
                        break
                    else:
                        print("Hatalı giriş! Geçerli bir seçim yapın.")

                if secim == "1":
                    while True:
                        yeni_soyad = input("Yeni soyadı: ")
                        if yeni_soyad.isalpha():
                            break
                        else:
                            print("Hatalı giriş! Soyadı sadece harflerden oluşmalıdır. Tekrar deneyin.")
                    ogrenci[1] = yeni_soyad
                elif secim == "2":
                    while True:
                        yeni_yas = input("Yeni yaş: ")
                        if yeni_yas.isdigit():
                            break
                        else:
                            print("Hatalı giriş! Yaş sadece sayılardan oluşmalıdır. Tekrar deneyin.")
                    ogrenci[2] = yeni_yas
                elif secim == "3":
                    while True:
                        yeni_kredi = input("Yeni kredi: ")
                        if yeni_kredi.isdigit():
                            break
                        else:
                            print("Hatalı giriş! Kredi sadece sayılardan oluşmalıdır. Tekrar deneyin.")
                    ogrenci[3] = yeni_kredi

                ogrencileri_kaydet(ogrenciler)
                print("Öğrenci bilgisi güncellendi.")
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")
    except Exception as e:
        print("Öğrenci güncellenirken bir hata oluştu:", str(e))



def ogrenci_ara():
    try:
        ad = input("Aranacak öğrencinin adını girin: ")
        bulundu = False
        for ogrenci in ogrenciler:
            if ogrenci[0] == ad:
                print("Ad:", ogrenci[0])
                print("Soyad:", ogrenci[1])
                print("Yaş:", ogrenci[2])
                print("Kredi:", ogrenci[3])
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")

        devam = input("Ana menüye dönmek için 'H'ye basın: ")
        if devam.upper() == "H":
            return  # Ana menüye dön
        else:
            print("Hatalı giriş! Geçerli bir seçim yapın.")
    except Exception as e:
        print("Öğrenci aranırken bir hata oluştu:", str(e))


def ogrenci_sil():
    try:
        ad = input("Silinecek öğrencinin adını girin: ")
        bulundu = False
        for ogrenci in ogrenciler:
            if ogrenci[0] == ad:
                ogrenciler.remove(ogrenci)
                ogrencileri_kaydet(ogrenciler)
                print("Öğrenci silindi.")
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")

        devam = input("Ana menüye dönmek için 'H'ye basın: ")
        if devam.upper() == "H":
            return  # Ana menüye dön
        else:
            print("Hatalı giriş! Geçerli bir seçim yapın.")
    except Exception as e:
        print("Öğrenci silinirken bir hata oluştu:", str(e))


def listele():
    try:
        for ogrenci in ogrenciler:
            print("Adı:", ogrenci[0])
            print("Soyadı:", ogrenci[1])
            print("Yaşı:", ogrenci[2])
            print("Kredisi:", ogrenci[3])
            print("-----------------------")

        devam = input("Ana menüye dönmek için 'H'ye basın: ")
        if devam.upper() == "H":
            return  # Ana menüye dön
        else:
            print("Hatalı giriş! Geçerli bir seçim yapın.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))


def genel_not_ortalamasi_hesapla():
    try:
        ad = input("Not ortalamasını hesaplamak istediğiniz öğrencinin adını girin: ")
        bulundu = False
        for ogrenci in ogrenciler:
            if ogrenci[0] == ad:
                dersler = ["Matematik", "Fizik", "Kimya"]  # Örnek olarak ders isimlerini bir tuple olarak tanımladım

                ders_notlari = []
                for ders in dersler:
                    vize_notu = float(input(ders + " vize notunu girin: "))
                    final_notu = float(input(ders + " final notunu girin: "))
                    ders_ortalama = vize_notu * 0.4 + final_notu * 0.6
                    print(ders, "not ortalaması:", ders_ortalama)
                    ders_notu = [ders, vize_notu, final_notu, ders_ortalama]  # Tuple yerine list kullanıldı
                    ders_notlari.append(ders_notu)

                genel_ortalama = sum(ortalama for _, _, _, ortalama in ders_notlari) / len(dersler)
                print(ad, "adlı öğrencinin genel not ortalaması:", genel_ortalama)

                ogrenci.extend(ders_notlari)  # Öğrenciye notları ekledik
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")

        while True:
            secim = input("Devam etmek için 'D', ana menüye dönmek için '0', not değiştirmek için 'N' tuşuna basın: ")
            if secim.upper() == 'D':
                break  # Devam et
            elif secim == '0':
                return  # Ana menüye dön
            elif secim.upper() == 'N':
                ad = input("Notlarını değiştirmek istediğiniz öğrencinin adını girin: ")
                for ogrenci in ogrenciler:
                    if ogrenci[0] == ad:
                        for ders in ders_notlari:
                            ders_adi = ders[0]
                            secilen_ders = input(f"{ders_adi} için not değiştirmek istiyor musunuz? (E/H): ")
                            if secilen_ders.upper() == 'E':
                                secilen_not = input("Vize mi yoksa final mi notunu değiştirmek istiyorsunuz? (V/F): ")
                                if secilen_not.upper() == 'V':
                                    yeni_vize = float(input(ders_adi + " yeni vize notunu girin: "))
                                    ders_notlari[ders_notlari.index(ders)][1] = yeni_vize  # Vize notunu güncelle
                                elif secilen_not.upper() == 'F':
                                    yeni_final = float(input(ders_adi + " yeni final notunu girin: "))
                                    ders_notlari[ders_notlari.index(ders)][2] = yeni_final  # Final notunu güncelle
                                else:
                                    print("Geçersiz seçim. Lütfen 'V' veya 'F' tuşlarından birini girin.")
                                break
                        else:
                            print("Ders bulunamadı.")
                        break
                else:
                    print("Öğrenci bulunamadı.")
            else:
                print("Geçersiz seçim. Lütfen 'D', '0' veya 'N' tuşlarından birini girin.")

    except ValueError:
        print("Geçersiz not girdisi. Notlar sayısal bir değer olmalıdır.")
    except Exception as e:
        print("Hata oluştu:", str(e))

def ogrenci_harc_parasi_hesapla():
    try:
        ad = input("Öğrenci adını girin: ")
        bulundu = False
        for ogrenci in ogrenciler:
            if ogrenci[0] == ad:
                kredi = int(ogrenci[3])
                harc_ucreti = kredi * 20
                print("Öğrencinin harç parası:", harc_ucreti)
                bulundu = True
                break

        if not bulundu:
            print("Öğrenci bulunamadı.")
    except Exception as e:
        print("Hata oluştu:", str(e))


def menu():
    ogrenciler = ogrencileri_yukle()

    while True:
        print("------ MENU ------")
        print("1. Öğrenci Ekle")
        print("2. Öğrenci Güncelle")
        print("3. Öğrenci Ara")
        print("4. Öğrenci Sil")
        print("5. Öğrenci listele")
        print("6. Not Ortalaması Hesapla")
        print("7. Öğrenci Harç Parası Hesapla")
        print("0. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_guncelle()
        elif secim == "3":
            ogrenci_ara()
        elif secim == "4":
            ogrenci_sil()
        elif secim == "5":
            listele()
        elif secim == "6":
            genel_not_ortalamasi_hesapla()
        elif secim == "7":
            ogrenci_harc_parasi_hesapla()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


menu()
