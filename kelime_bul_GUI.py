# -*- coding: utf-8 -*-

from faulthandler import disable
from sre_parse import State
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, messagebox

#Fonksiyonlar

def ara():
    
    cikti.delete("1.0",tk.END)

    with open("Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
        liste = dosya.readlines()
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"     

        for harf in girdi.get():
            if harf not in alfabe or girdi.get() == "Lütfen geçerli karakter yazın":
                messagebox.showerror("Hatalı Karakter!","izin verilen harflerin disinda bir veya daha fazla harf yazdiginiz icin, isleme devam edilemiyor!\nKullanılabilir karakterler şunlardır:\nabcçdefgğhıijklmnoöprsştuüvyz")
                girdi.delete(0, tk.END)
                break

            
            else:
                deger = 0
                aranan = girdi.get()
                
                for kelime in liste:
                    for harf in aranan:
                        if harf in kelime[:-1]:
                            deger += 1
                    
                    if deger == len(aranan):
                        icerik = cikti.get("1.0", END)
                        if kelime not in icerik:
                            cikti.insert(END,kelime)

                    deger = 0
                
                if (int(cikti.index("end")[:-2]) - 2 == 0):
                    sonuc["text"] = "Sonuç bulunamadı."

                else:
                    sonuc_sayi = int(cikti.index("end")[:-2])    
                    sonuc["text"] = "Toplam " + str(sonuc_sayi - 2) + " sonuç bulundu."

def kaydet():
    with open("sonuc.txt", "w", encoding="UTF-8") as dosya:
        dosya.write("'" + girdi.get() + "' Karakterlerini barındıran kelime araması sonucu " + cikti.index("end")[:-2] + " adet sonuç bulunmuştur.\nArama sonucu bulunan kelimeler, aşağıda listelenmiştir.\n\n" + cikti.get("1.0","end"))

def temizle():
    girdi.delete(0, tk.END)
    cikti.delete("1.0",tk.END)
    sonuc["text"] = ""

arkaplan_rengi = "#17a589"
arkaplan_rengi_metin = "#d1f2eb"
arkaplan_rengi_buton = "#17a589"

pencere = tk.Tk()
pencere.geometry("300x450+600+300")
pencere.resizable("FALSE", "FALSE")
pencere.title("Kelime Bul ve Listele")
pencere.configure(bg = arkaplan_rengi)

# Arayüz Unsurlarının (Widget) Yerleşimi
aciklama = tk.Label(pencere, text = "Aradığınız kelimeye ait harfleri,\naralarında boşluk bırakmadan \naşağıdaki kutuya  yazın. Ör. tryk",
                    fg = "white",
                    bg = arkaplan_rengi,
                    font = "Verdana 11",
                    width=32)
aciklama.place(x=4, y=10)

girdi = tk.Entry(pencere, 
                width=34,
                bg = arkaplan_rengi_metin)
girdi.place(x=10, y=80)

cikti = tk.Text(pencere,
                width=34,
                height=14,
                state="normal",
                bg = arkaplan_rengi_metin)
cikti.place(x=10, y=110)

sonuc = tk.Label(pencere,
                text = "",
                font = "Verdana 10 bold",
                fg = "white",
                bg = arkaplan_rengi)
sonuc.place(x=10, y= 357)                

btn_genisligi = 12

btn_ara = tk.Button(pencere,
                    text = "Ara",
                    width = btn_genisligi,
                    font = "Verdana 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    command= ara)
btn_ara.place(x=10, y=380)

btn_temizle = tk.Button(pencere,
                    text = "Temizle",
                    width = btn_genisligi,
                    font = "Verdana 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    command= temizle)
btn_temizle.place(x=150, y=380)


btn_kaydet = tk.Button(pencere,
                    text = "Kaydet",
                    width = btn_genisligi,
                    font = "Verdana 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "white",
                    command= kaydet)
btn_kaydet.place(x=10, y=415)

btn_kapat = tk.Button(pencere,
                    text = "Kapat",
                    width = btn_genisligi,
                    font = "Verdana 10 bold",
                    bg = "#cd6155",
                    fg = "white",
                    command=quit)
btn_kapat.place(x=150, y=415)

pencere.mainloop()