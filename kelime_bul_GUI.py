# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, messagebox

#Fonksiyonlar

def ara():
    
    cikti.delete("1.0",tk.END)

    with open("Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
        liste = dosya.readlines()
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"     

        for harf in girdi.get().lower():
            if harf not in alfabe:
                messagebox.showerror("Hatalı Karakter!","İzin verilen karakterlerin dışında bir veya daha fazla karakter yazdığınız için, işleme devam edilemiyor!\nKullanılabilir karakterler şunlardır:\nabcçdefgğhıijklmnoöprsştuüvyz")
                girdi.delete(0, tk.END)
                sonuc["text"] = ""
                break

            
            else:
                deger = 0
                aranan = girdi.get().lower()
                
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
                    btn_kaydet.configure(state = "normal")

def kaydet():
    with open("sonuc.txt", "w", encoding="UTF-8") as dosya:
        bulunan_kelime = str(int(cikti.index("end")[:-2]) - 2)
        dosya.write("'" + girdi.get() + "' Karakterlerini barındıran kelime araması sonucu " + bulunan_kelime + " adet sonuç bulunmuştur.\nArama sonucu bulunan kelimeler, aşağıda listelenmiştir.\n\n" + cikti.get("1.0","end"))

def temizle():
    girdi.delete(0, tk.END)
    cikti.delete("1.0",tk.END)
    sonuc["text"] = ""
    btn_kaydet.configure(state = "disabled")

def pencere_hakkinda():     # "Hakkında" Penceresinin Özellikleri ve Metni                      
    hakkinda = tk.Toplevel()
    hakkinda.title("Hakkında")
    hakkinda.geometry("300x125")
    hakkinda.resizable("FALSE", "FALSE")
    bilgi = tk.Label(hakkinda, text="\nKelime Bul, Listele ve Kaydet\n\nKodlayan: Mustafa Halil\n\nhttps://github.com/mhalil\n")
    bilgi.pack()

    
# Pencere Ebatları ve Renk Tanımları
arkaplan_rengi = "#17a589"
arkaplan_rengi_metin = "#d1f2eb"
arkaplan_rengi_buton = "#17a589"

pencere = tk.Tk()
pencere.geometry("300x450+600+300")
pencere.resizable("FALSE", "FALSE")
pencere.title(".:: Kelime Bul ::.")
pencere.configure(bg = arkaplan_rengi)

# Arayüz Unsurlarının (Widget) Yerleşimi

menu_cubugu = tk.Menu(pencere)
pencere.config(menu=menu_cubugu) #menümüzü oluşturduk

dosya_menusu = tk.Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Dosya", menu=dosya_menusu)
dosya_menusu.add_command(label="Kapat", command=pencere.quit)

hakkinda_menusu = tk.Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Hakkında", menu=hakkinda_menusu)
hakkinda_menusu.add_command(label="Hakkında", command=pencere_hakkinda)   

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
                    state = "disable",
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