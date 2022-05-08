# tkinter ile arayüz oluşturulacak.
# sonucun dosyaya kaydedilmesi, "Kaydet" butonu sayesinde gerçekleşecek.

from faulthandler import disable
from pickle import FALSE
import tkinter as tk
from tkinter import DISABLED, END, messagebox
from tkinter.font import NORMAL
from turtle import right

#Fonksiyonlar

def ara():
    with open("TDK_Sozluk_Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
        liste = dosya.readlines()
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

        for harf in girdi.get():
            if harf not in alfabe or girdi.get() == "Lütfen geçerli karakter yazın":  # Hatayı tek sefer almam lazım, geçersiz karakter sayısı kadar değil!
                print("Hata!, Geçersiz Karakterler")
                messagebox.showerror("Hatalı Karakter!","izin verilen harflerin disinda bir veya daha fazla harf yazdiginiz icin, isleme devam edilemiyor!\nKullanılabilir karakterler şunlardır:\nabcçdefgğhıijklmnoöprsştuüvyz")

            puan = 0
            for kelime in liste:
                for harf in girdi.get():
                    if harf in kelime[:-1]:
                        puan += 1
                if puan >= len(girdi.get()):
                    cikti.insert(END,kelime)
                    
                puan = 0


def kaydet():
    pass

def temizle():
    girdi.bind = girdi.delete(0,END)
    cikti.delete("1.0","end")

pencere = tk.Tk()
pencere.geometry("300x450+600+300")
pencere.resizable("FALSE", "FALSE")
pencere.title("Kelime Üret")

# messagebox.showinfo("Bilgi !", "Bu Uygulama, Kullanıcının belirttiği sesli/sessiz harfleri içeren kelimeleri Türkçe Sozlük dosyasında tarayarak, eşleşen kelimeleri listeler.")

aciklama = tk.Label(pencere, text = "Bulmak istediğiniz kelimeye ait \nHarfleri, aralarında boşluk bırakmadan \naşağıdaki kutuya  yazın;",
                    # bg = "yellow",
                    fg = "blue",
                    font = "Tahoma 10")
aciklama.place(x=20, y=10)

girdi = tk.Entry(pencere, width=34)
girdi.insert(0,"Lütfen geçerli karakter yazın")

girdi.place(x=10, y=80)

cikti = tk.Text(pencere,
                width=31,
                height=15,
                state="normal")
cikti.place(x=10, y=110)

kaydirma_cubugu = tk.Scrollbar(pencere,
                                width=15, 
                                command=cikti.yview,
                                orient="vertical")
kaydirma_cubugu.place(x=270, y=110)



btn_genisligi = 12

btn_ara = tk.Button(pencere,
                    text = "Ara",
                    width = btn_genisligi,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    # state=DISABLED,
                    command= ara)
btn_ara.place(x=10, y=380)

btn_temizle = tk.Button(pencere,
                    text = "Temizle",
                    width = btn_genisligi,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command= temizle)
btn_temizle.place(x=150, y=380)


btn_kaydet = tk.Button(pencere,
                    text = "Kaydet",
                    width = btn_genisligi,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command= kaydet)
btn_kaydet.place(x=10, y=415)

btn_kapat = tk.Button(pencere,
                    text = "Kapat",
                    width = btn_genisligi,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command=quit)
btn_kapat.place(x=150, y=415)

pencere.mainloop()