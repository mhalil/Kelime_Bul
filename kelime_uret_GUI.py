# tkinter ile arayüz oluşturulacak.
# sonucun dosyaya kaydedilmesi, "Kaydet" butonu sayesinde gerçekleşecek.

from faulthandler import disable
from pickle import FALSE
import tkinter as tk
from tkinter import messagebox

#Fonksiyonlar

def ara():
    with open("TDK_Sozluk_Kelime_Listesi.txt", "r", encoding="UTF-8") as dosya:
        liste = dosya.readlines()
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

        for harf in girdi:
            if harf not in alfabe:
                messagebox.showerror("Hatalı Karakter!","izin verilen harflerin disinda bir veya daha fazla harf yazdiginiz icin, isleme devam edilemiyor!")
 


def kaydet():
    pass


pencere = tk.Tk()
pencere.geometry("300x400+600+300")
pencere.resizable("FALSE", "FALSE")
pencere.title("Kelime Üret")

# messagebox.showinfo("Bilgi !", "Bu Uygulama, Kullanıcının belirttiği sesli/sessiz harfleri içeren kelimeleri Türkçe Sozlük dosyasında tarayarak, eşleşen kelimeleri listeler.")

aciklama = tk.Label(pencere, text = "Bulmak istediğiniz kelimeye ait \nHarfleri, aralarında boşluk bırakmadan \naşağıdaki kutuya  yazın;",
                    # bg = "yellow",
                    fg = "blue",
                    font = "Tahoma 10")
aciklama.place(x=20, y=10)

girdi = tk.Entry(pencere, width=34)
girdi.place(x=10, y=80)

cikti = tk.Text(pencere,
                width=34,
                height=14,
                state="disabled")
cikti.place(x=10, y=110)

btn_ara = tk.Button(pencere,
                    text = "Ara",
                    width=7,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command= ara)
btn_ara.place(x=10, y=360)

btn_kaydet = tk.Button(pencere,
                    text = "Kaydet",
                    width=7,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command= kaydet)
btn_kaydet.place(x=105, y=360)

btn_kapat = tk.Button(pencere,
                    text = "Kapat",
                    width=7,
                    # bg = "Yellow",
                    # fg = "red",
                    font = "Tahoma 10 bold",
                    command=quit)
btn_kapat.place(x=200, y=360)

pencere.mainloop()