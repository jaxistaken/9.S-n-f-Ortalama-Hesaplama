#edited By& umuth.py
#9.Sınıflara Özel Yapılmıştır Okulumuza Hoş Geldiniz :)

from tkinter import *

pencere=Tk()
pencere.title("Fen Lisesi 9.Sınıf Ortalama Hesaplama")
pencere.geometry("900x700+0+0")
#----
b=Label(text="               ")
b.grid(row=0,column=2)
#----
bedenl=Label(pencere,text="Beden Eğitimi:")
bedenl.config(font="bold 20",fg="white",bg="black")
bedenl.grid(column=1,row=0)
beden=Entry()
beden.config(font="bold 20")
beden.grid(column=3,row=0)

bilgisayarl=Label(pencere,text="Bilgisayar Bilimi:")
bilgisayarl.config(font="bold 20",fg="white",bg="black")
bilgisayarl.grid(column=1,row=1)
bilgisayar=Entry()
bilgisayar.config(font="bold 20")
bilgisayar.grid(column=3,row=1)

coğrafyal=Label(pencere,text="Coğrafya:")
coğrafyal.config(font="bold 20",fg="white",bg="black")
coğrafyal.grid(column=1,row=2)
coğrafya=Entry()
coğrafya.config(font="bold 20")
coğrafya.grid(column=3,row=2)

dinl=Label(text="Din Kültürü:")
dinl.config(font="bold 20",fg="white",bg="black")
dinl.grid(column=1,row=3)
din=Entry()
din.config(font="bold 20")
din.grid(column=3,row=3)

biyolojil=Label(text="Biyoloji:")
biyolojil.config(font="bold 20",fg="white",bg="black")
biyolojil.grid(column=1,row=4)
biyoloji=Entry()
biyoloji.config(font="bold 20")
biyoloji.grid(column=3,row=4)

fizikl=Label(text="Fizik:")
fizikl.config(font="bold 20",fg="white",bg="black")
fizikl.grid(column=1,row=5)
fizik=Entry()
fizik.config(font="bold 20")
fizik.grid(column=3,row=5)

kimyal=Label(text="Kimya:")
kimyal.config(font="bold 20",fg="white",bg="black")
kimyal.grid(column=1,row=6)
kimya=Entry()
kimya.config(font="bold 20")
kimya.grid(column=3,row=6)

mat=Label(text="Matematik:")
mat.config(font="bold 20",fg="white",bg="black")
mat.grid(column=1,row=7)
matematik=Entry()
matematik.config(font="bold 20")
matematik.grid(column=3,row=7)

müz=Label(text="Müzik:")
müz.config(font="bold 20",fg="white",bg="black")
müz.grid(column=1,row=8)
müzik=Entry()
müzik.config(font="bold 20")
müzik.grid(column=3,row=8)

alm=Label(text="Almanca:")
alm.config(font="bold 20",fg="white",bg="black")
alm.grid(column=1,row=9)
almanca=Entry()
almanca.config(font="bold 20")
almanca.grid(column=3,row=9)

sağ=Label(text="Sağlık Bilgisi:")
sağ.config(font="bold 20",fg="white",bg="black")
sağ.grid(column=1,row=10)
sağlık=Entry()
sağlık.config(font="bold 20")
sağlık.grid(column=3,row=10)

dik=Label(text="Diksiyon:")
dik.config(font="bold 20",fg="white",bg="black")
dik.grid(column=1,row=11)
diksiyon=Entry()
diksiyon.config(font="bold 20")
diksiyon.grid(column=3,row=11)

kur=Label(text="Kur'an-ı Kerim:")
kur.config(font="bold 20",fg="white",bg="black")
kur.grid(column=1,row=12)
kuran=Entry()
kuran.config(font="bold 20")
kuran.grid(column=3,row=12)

tar=Label(text="Tarih:")
tar.config(font="bold 20",fg="white",bg="black")
tar.grid(column=1,row=13)
tarih=Entry()
tarih.config(font="bold 20")
tarih.grid(column=3,row=13)

ede=Label(text="Edebiyat:")
ede.config(font="bold 20",fg="white",bg="black")
ede.grid(column=1,row=14)
edebiyat=Entry()
edebiyat.config(font="bold 20")
edebiyat.grid(column=3,row=14)

ing=Label(text="İngilizce:")
ing.config(font="bold 20",fg="white",bg="black")
ing.grid(column=1,row=15)
ingilizce=Entry()
ingilizce.config(font="bold 20")
ingilizce.grid(column=3,row=15)

boş=Label(text=" ")
boş.grid(column=1,row=16)

sonuç=Label(text="Notlarınızı Giriniz")
sonuç.config(font="bold 20",fg="white",bg="black")
sonuç.grid(column=2,row=17)
def a():
    top=(float(beden.get())*2+float(bilgisayar.get())*2+float(coğrafya.get())*2+float(din.get())*2+float(biyoloji.get())*2+float(fizik.get())*2+float(kimya.get())*2+float(matematik.get())*6+float(müzik.get())*2+float(almanca.get())*2+float(sağlık.get())*1+float(diksiyon.get())*1+float(kuran.get())*2+float(tarih.get())*2+float(edebiyat.get())*5+float(ingilizce.get())*4)/39
    sonuç.config(text=top)



buton1=Button()
buton1.config(text="Hesaplama",font="bold 20",command=a)
buton1.grid(column=4,row=17)

pencere.mainloop()

