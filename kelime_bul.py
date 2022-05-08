with open("TDK_Sozluk_Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
    liste = dosya.readlines()
#    print(satir)

    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    girdi = input("Kelime üretiminde kullanilacak harfleri, aralarinda bosluk olmadan ekleyin. Ornegin: trky.\nKullanilabilecek harfler : abcçdefgğhıijklmnoöprsştuüvyz \n:").lower()

    for harf in girdi:
        if harf not in alfabe:
            print("UYARI: izin verilen harflerin disinda bir veya daha fazla harf yazdiginiz icin, isleme devam edilemiyor!")
            break
        
        else:
            puan = 0
            for kelime in liste:
                for harf in girdi:
                    if harf in kelime[:-1]:
                        puan += 1
                if puan >= len(girdi):
                    print(kelime[:-1])
                    
                puan = 0
