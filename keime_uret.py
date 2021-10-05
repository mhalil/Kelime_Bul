with open("TDK_Sozluk_Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
    satir = dosya.read()

    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    girdi = input("Kelime üretiminde kullanilacak harfleri, aralarinda bosluk olmadan ekleyin. Ornegin: trky.\nKullanilabilecek harfler : abcçdefgğhıijklmnoöprsştuüvyz \n:").lower()

    for harf in girdi:
        if harf not in alfabe:
            print("UYARI: Yazilan metin icerisinde, Turkce alfabede olmayan karakter bulunduğu icin, isleme devam edilemiyor!")
            break

        else:
            for harf in girdi:
                if harf in satir:
                    print(satir)
