
###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8


y = 3.2


z = 8j + 18


a = "Hello World"


b = True


c = 23 < 22



l = [1, 2, 3, 4,"String",3.2, False]



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}


t = ("Machine Learning", "Data Science")



s = {"Python", "Machine Learning", "Data Science","Python"}



type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(o)
type(t)
type(s)

del x
del y
del z
del a
del b
del t
del s
del c
del o
###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

text.upper()
text.replace()
text.split()

#çok uzun yol
new_text =text.upper()
nw_text=""
for tex in new_text:
    if tex == ".":
        nw_text += " "
    elif tex == ",":
        nw_text += " "
    else:
        nw_text += tex

nwetext = nw_text.split()

#geminiden kısaltma yollarına baktım
#kısaltalım
text = "The goal is to turn data into information, and information into insight."

new_text =text.upper()
nw_text=""
for tex in new_text:
    if tex == "." or tex == ",":      # burada or kullanarak elif kodunu çıkarttık ve kod daha çok kısaldı
        nw_text += " "
    else:
        nw_text += tex

nwetext = nw_text.split()


#2. kısaltma

new_text =text.upper()
nw_text=""
for tex in new_text:
    if tex in [",","."]:      # burada in kullanarak liste halinde kullanarak daha kısaldı
        nw_text += " "
    else:
        nw_text += tex

nwetext = nw_text.split()


#3. kısaltma

new_text =text.upper()
nw_text= new_text.replace(","," ").replace(".", " ")   # burada döngüyü çıkartıp replace fonksiyonuyla önce noktaları sonra virgülleri boşluğa çeviriyoruz
nwetext = nw_text.split()

#4. kısaltma
# tek satırda method zincirleme kullanarak yapıyoruz buna method channing deniyormuş
new_text= text.upper().replace(","," ").replace(".", " ") .split()


del nwetext
del new_text
del nw_text
del text


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.

len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.

lst[0],lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

list=lst[0:4]
#başka yollar
#1
nwlist = lst[:4]  # Sıfırı yazmadık, Python otomatik sıfır kabul etti.
#2
nwlist = []
for index, harf in enumerate(lst):
    if index < 4:  # İndeks 0, 1, 2, 3 ise listeye ekle
        nwlist.append(harf)


# Adım 4: Sekizinci index'teki elemanı silin.

lst.replace(lst[8],"") #benim yaptığım haralı

#1.
lst.pop(8)

#2.
del lst[8]

# Adım 5: Yeni bir eleman ekleyin.

lst.append("k")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8,"N")


del lst
###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.


dict["Daisy"]  #benim yaptığım   eksik  başarısız x
dict["Daisy"][1]=13

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict["Ahmet"]=["Turkey",24]

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"] # bu tamamen yok ediyor

dict.pop("Antonio") # bu sadece sözlükten çıkarıyor ama verileri başka yerde kullanılabilir şeklinde saklıyor

del dict
###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]
# fonksiyon yapmayı unutup sadece döngüyle yaptım  !!!!!!!!!!!! dikkat et soruya
t=[]
c=[]
for i in l:
    if i%2==0:
        c.append(i)
    else:
        t.append(i)

#sadece t ve c listeleri fonksiyona dahil ederek daha profesyonel gözükecek şekilde bir düzeltme oldu
def tekcif(deger):
    t = []
    c = []
    for i in deger:
        if i % 2 == 0:
            c.append(i)
        else:
            t.append(i)
    return c,t

tekcif(l)

#kısa yol
def tekcif(deger):
    t = [i for i in deger if i%2!=0]
    c = [i for i in deger if i%2==0]
    return c,t

tekcif(l)

del t
del c
del tekcif
del i
del l
###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
#benim yaptıklarım yanlış değil ama ben sadece fakülteye ayırdım ekrana yazdırmadım sebebi soruda bizden çıktısını fakuülteleriyle beraber yazdırmamızı istemiş
def fklt(ogr):
    m=[]
    t=[]
    for i,ad in enumerate(ogr):
        if i<3:
            m.append(ad)
        else:
            t.append(ad)
    return m,t

fklt(ogrenciler)

#kısa sı
def fklt(ogr):
    m=[ad for i,ad in enumerate(ogr) if i<3]
    t=[ad for i,ad in enumerate(ogr) if i>2]
    return m,t

fklt(ogrenciler)
# bu istediğimiz sonucu veriyor ancak belleği boş yere yoruyor
def fklt(ogr):
    fklt_lst=[print("mühendislik fakültesi sırası :" ,i+1 ," öğrenci : ",ad) if i<3 else print("tıp fakültesi sırası :" ,i-2 ," öğrenci : ",ad) for i,ad in enumerate(ogr)]

fklt(ogrenciler)
## doğrusu (tercihen bu daha düzenli alttakinden)

def fklt(ogr):
    for i,ad in enumerate(ogr):
        if i<3:
             print(f"Mühendislik Fakültesi {i + 1}. öğrenci: {ad}")           #buradaki süslü parantezlerin içini kod olarak algılıyor string olarak değil.
        else:
             print(f"Tıp Fakültesi {i - 2}. öğrenci: {ad}")

fklt(ogrenciler)

#tek satırda yapılan bir versiyon

def fklt(ogr):
    for i, ad in enumerate(ogr):
        print("mühendislik fakültesi sırası :", i + 1, "öğrenci :", ad) if i < 3 else print("tıp fakültesi sırası :", i - 2, "öğrenci :", ad)

fklt(ogrenciler)
del ogrenciler
del fklt
del m
del t
###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

zip(ders_kodu,kredi,kontenjan)
#doğru
for kod,krd,kon in zip(ders_kodu,kredi,kontenjan):
    print(kod,krd,kon)
# bu da açıklamalı
for kod, krd, kon in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders: {kod} | Kredi: {krd} | Kontenjan: {kon}")

del ders_kodu
del kredi
del kontenjan
del kon
del kod
del krd

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

#adım adım destekli yapıyorum
#burada küme 1 küme ikiyi kapsıyor mu onu kontrol ettik
kume1.issuperset(kume2)
#kesişen elemanlara baktık
kume1.intersection(kume2)

#burada küme 2 biri kapsıyor mu ona baktık
kume2.issuperset(kume1)
#küme 2 de olup küme 1 de olmayan elemanları yazdırır
kume2.difference(kume1)

#burayı mantığını anladıktan sonra ve bilgileri hatırladıktan sonra kendim yazıyorum

def altkm(km1,km2):
    if km1.issuperset(km2):
        print(km1.intersection(km2))
    else:
        print(km1.difference(km2))          # ahahah hata yaptık yine burada tam tersini koymam lazımdı print(km2.difference(km1)) şeklinde olması gerekiyordu !!!!!!!!!!!!!!! amanin dikkat!!!!!!!!!!!!

altkm(kume1,kume2)

#doğrusu

def altkm(km1,km2):
    if km1.issuperset(km2):
        print(km1.intersection(km2))
    else:
        print(km2.difference(km1))          # ahahah hata yaptık yine burada tam tersini koymam lazımdı print(km2.difference(km1)) şeklinde olması gerekiyordu !!!!!!!!!!!!!!! amanin dikkat!!!!!!!!!!!!

altkm(kume1,kume2)
#bonus
altkm(kume2,kume1)

del altkm
del kume1
del kume2
#genelde fonksiyonları sabit değerlerle değilde yeni argümanla beraber kullanarak, özel bir fonksiyondan çok genel kullanabileceğim şekilde yapmaya ve alıştırmaya çalışıyorum







##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()
#hata yaptık yine
[f"NUM_{col.upper()}" if df[col].dtype(O) else col for col in df.columns]

#soruda abbrev i büyük istemiyor ama örnek çıktıda büyük olduğu için örnek çıktıya göre yaptım

#doğrusu
[f"NUM_{col.upper()}" if df[col].dtype!="O" else col.upper() for col in df.columns]



# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']

#burada bir kaç hatam vardı biri upper ın parantezini unutmuşum diğeride if te not in yerine in yapıp sorunun istediğinin tam tersini yapmışım ufak bir rütuşla mükemmel :)

[f"{col.upper()}_FLAG"  if "no" not in col else col.upper() for col in df.columns]



# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

#hatalar bitmiyor...
#del List Comprehension İçinde Çalışmaz ve amacımız silmek değil diğerlerini seçmekmiş
new_df = [del.df.colums[col] for col in df.columns if col in og_list]

#yeni deneme

new_df=[col for col in df.columns if col not in og_list]

#buradaki hata biz bunu new_cols olarak kaydetmemiz gerekiyormuş data frame değil bir isim sütunu

new_cols=[col for col in df.columns if col not in og_list]

new_df = df[new_cols]



del new_df