

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
from rich import columns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset("titanic")

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df["sex"].value_counts()


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df["pclass"].unique()


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df[["pclass","parch"]].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype


#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df["embarked"  == "C" ] # bu yanlış mantık hatası sütndaki değerlerin c ye denk olduğunu kontol edilmesi gerek ama burada embarked ın c ye denk olduğunu söylemiş olduk


df[df["embarked"] == "C"] # doğrusu

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"] != "S"]

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df[[df["sex"]=="woman" & df["age"] < 30]]  # HATA!! koşulları ayrı ayrı normal paranteze almam gerekiyordu ve woman değil female yanlış sütuna bakmışım

df[(df["sex"]=="female") & (df["age"] < 30)]

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df["fare"] > 500) | (df["age"] > 70)]


#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df["who"].drop() # burada who sütunun içindekileri silmeye çalışıyoruz ama sütunu silmemiz isteniyor

ndf = df.drop("who" , axis = 1)  # bunu yaparak eski df bozmadan yeni şeklini yeni bir df e atadık

df.drop("who" , axis = 1, inplace = True)   # eğer bu şekilde yaparsak mevcut df üzerinde dğişiklik yapmış oluruz


df = sns.load_dataset("titanic")
df.columns
ndf.columns
del df

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df["deck"].mode()[0] # 0 ekleyerek listenin ilk elemanını yani ençok tekrar eden elemanını verir

df["deck"]=df["deck"].fillna(df["deck"].mode()[0])


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df["age"] = df["age"].fillna(df["age"].median())

#kontrol

df["age"].isnull().sum()

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

# burada kırılımını istediğimiz değişkenleri ve sonra hangi durumu incemek istediğimizi son olarak da bizden istenilen işlemleri yaparız

df.groupby(["pclass", "sex"])["survived"].agg(["sum","count", "mean"])

#pivot table ile yapan var

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

lambda x: 1 if x < 30 else 0  # Burada 30 dan küçük veya eşit olma durumunda yapılaxakları lambda ile gösteriyoruz

df["age"].apply(lambda x: 1 if x < 30 else 0) # Burada işlemi sütuna uyguluyoruz

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)  # burada işlmleri yeni sütuna atıyoruz

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df= sns.load_dataset("tips")


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby("time")["total_bill"].agg(["sum","min","max","mean"])

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby(["day", "time"])["total_bill"].agg(["sum","min","max","mean"])

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

[(df["time"] == "Lunch") & (df["sex"] == "female")]

# filtrelemeyi yanlış yere yaptık  ve day i unuttuk

df.groupby([(df["time"] == "Lunch") & (df["sex"] == "female")])["total_bill"].agg(["sum","min","max","mean"])


df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day")[["total_bill", "tip"]].agg(["sum", "min", "max", "mean"])

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df.head()
df[(df["size"] < 3) & (df["total_bill"] > 10)].mean()

df[(df["size"] < 3) & (df["total_bill"] > 10)].mean(numeric_only=True)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].mean(numeric_only=True)

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

# sort_values ile sıralama yapıyoruz ascending=False ile sırayı büyükten küçüğe çeviriyoruz true hali küçükten büyüğe

new_df = df.sort_values(by="total_bill_tip_sum", ascending=False).head(30)
new_df.head()



del df
del new_df








#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

import numpy as np
import seaborn as sns
import pandas as pd
from rich import columns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("persona.csv")

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()

df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df.head()

df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum() #burada satıra yerleştiriyoruz

df.groupby("COUNTRY", as_index=False)["PRICE"].sum() #burada sütunda tutmaya devam ediyoruz

df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="sum") # veriyi daha okunaklı toblo olarak verir

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?

df["SOURCE"].value_counts()

df.groupby("SOURCE")["PRICE"].count()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()

df.pivot_table("PRICE", "COUNTRY", aggfunc="mean")

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()

df.pivot_table( "PRICE", "SOURCE", aggfunc="mean")

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean()

df.pivot_table( "PRICE", ["COUNTRY","SOURCE"], aggfunc="mean")

#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################

df.head()

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()

df.pivot_table("PRICE",["COUNTRY", "SOURCE", "SEX", "AGE"], aggfunc="mean")

#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean().sort_values(ascending=False)

df.pivot_table("PRICE",["COUNTRY", "SOURCE", "SEX", "AGE"], aggfunc="mean").sort_values(by="PRICE", ascending=False)

del agg_df

#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
agg_df.head()
del agg_df["AGE_GRP"]

#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

age_bins = [0, 18, 23, 30, 40, 70]

age_labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]

agg_df["AGE_GRP"] = pd.cut(agg_df["AGE"], bins=age_bins, labels=age_labels ) # burada age e atamadım sebebi doğru olup olmadığını görmek için

agg_df["AGE"] = pd.cut(agg_df["AGE"], bins=age_bins, labels=age_labels )


#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df["customers_level_based"] = (agg_df["COUNTRY"].astype(str) + "_" +
                                   agg_df["SOURCE"].astype(str) + "_" +
                                   agg_df["SEX"].astype(str) + "_" +
                                   agg_df["AGE"].astype(str)).str.upper()

agg_df["customers_level_based"] = [f"{col[0]}_{col[1]}_{col[2]}_{col[3]}".upper() for col in agg_df.values]
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()
del agg_df["customers_level_based"]

agg_df.groupby("customers_level_based")["PRICE"].mean().reset_index()

agg_df.pivot_table("PRICE","customers_level_based", aggfunc="mean").head()

#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels=["D", "C", "B", "A"])
segment_summary = agg_df.groupby("SEGMENT")["PRICE"].agg(["mean", "max", "min", "count", "sum"])
print(segment_summary)

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user_1 = "TUR_ANDROID_FEMALE_31_40"
result_1 = agg_df[agg_df["customers_level_based"] == new_user_1]
print(result_1)

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

new_user_2 = "FRA_IOS_FEMALE_31_40"
result_2 = agg_df[agg_df["customers_level_based"] == new_user_2]
print(result_2)


