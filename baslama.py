#ekrandan girilen sayının asal olup olmadığını kontrol eden program:
##sayi=int(input("Bir sayı giriniz:"))
#for i in range (2,sayi):
#    if sayi % i == 0:
 #       print("sayı asal değildir")
  #      break 
   # else:
    #    if i>=sayi:
     #    print("sayı asaldır")
     #    break
 #hata veriyor
 #doğru cevap:
#sayi=int(input("Bir sayı giriniz:"))
#prime =True #sayının asal olduğunu kabul ettik
#for i in range (2,sayi):
 #   if sayi %i ==0:
  #      prime=False
  #      break 
#if prime == True :
 #   print(f"{sayi}sayısı asaldır")
#else:
 #   print(f"{sayi}sayısı asal değildir")
 
#ekrandan girilen sayının kaç tane pozitip tam böleni olduğunu bulan program:
#sayi=int(input("Bir sayı giriniz:"))
#bolen_sayisi=0
#for i in range(1,sayi+1):
#      if sayi%i == 0:
#            bolen_sayisi +=1
#print(f"{sayi}sayısının {bolen_sayisi} kadar böleni vardır")


#ekrandan okunan bir sayının rakamları toplamaını hesaplayan bir program yazınız
#1.yol
#sayi=int(input("Bir sayı giriniz:"))
#str_sayi=str(sayi)
#toplam=0
#for rakam in str_sayi:
#      toplam +=int(rakam)
#print(toplam)
#2.yol
#sayi=int(input("Bir sayo giriniz:"))
#gecici_sayi=sayi
#toplam=0
#while gecici_sayi != 0:
#      basamak= gecici_sayi % 10
#      toplam += basamak
#      gecici_sayi //= 10
#print(toplam)     
 
#ekrandan okunan peş peşe okunan beş sayının en küçüğünü ve en büyüğünü ekrana yazdıran program:

#liste=[]
#for i in range(5):
#     sayi=int(input("bir sayı giriniz:"))
#     liste.append(sayi)
#print(f"en büyük sayi: {max(liste)}")
#print(f"en küçük sayi: {min(liste)}")


#ekrandan okunan bir sayının herhangi bir sayının karesi olup olmadığını kontrol eden program:

#sayi=int(input("bir sayı giriniz:"))
#karekok=sayi ** 0.5
#if karekok == int(karekok):
#      print("tamkaredir")
#      print(karekok)
#else:
#      print("tamkare değildir")


#ekrandan okunan bir mwtinde hangi harfin kaç kere kullanıldığını gösteren program:

#metin=input("bir metin giriniz:")
#sozluk=dict()
#for harf in metin:
#      if harf in sozluk:
#          sozluk[harf]+=1
#      else:
#          sozluk[harf] =1
#for harf,adet in sozluk.items():
#      print(harf,adet)


#ekrandaan okunan bir metinde a harflerini büyük yapan bir program:

#metin=input("bir metin giriniz:")
#metin2=""
#for harf in metin:
#      if harf=="a":
#            metin2 += "A"
#      else:
#            metin2 += harf
#print(metin2)   


#ilk 10.000 asal sayının kaç tanesi 3 ile başlar 7 ile biter?

#prime_list=list()      
#prime_list.append(2)
#sayi=3
#while True:
#      prime=True
#      for i in range (2,sayi):
#            if sayi%i == 0:
#                  prime= False 
#                  break
#      if prime: #prime==True da diyebiliriz
#        prime_list.append(sayi)
#        if len(prime_list)==10000:
#              break
#      sayi +=1
#liste2=list()
#for prime in prime_list:
#      strprime=str(prime)
#      if strprime.startswith("3") and strprime.endswith("7"):
#            liste2.append(prime)
#print(liste2)
#print(len(liste2))
#10.000 tane sayıyı bu şekilde kontrol etmek zor olacağından biz direkt sadece sayının karekökünden bir fazlasına kadar olan kısma 
#bakabiliriz yine aynı sonucu verecektir ama daha hızlı olacaktır.
#104.satırdaki yeri for i in range (2.sayi**0.5+1) olarak değiştirebiliriz.

#3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir?

#liste=list()
#for sayi in range (100,1000):
#    toplam=0
#    gecici_sayi=sayi
#    while gecici_sayi!=0:
#          basamak = gecici_sayi%10
#          toplam += basamak**3
#          gecici_sayi//=10
#    if toplam == sayi:
#          liste.append(sayi)
#print(liste)
  

#ilk 100 fibonacci sayısını ekrana yazdıran program:
#1.yol
#fibonacci_list=list()
#fibonacci_list.append(1)
#fibonacci_list.append(1)
#index=2
#while True:
#      fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#      index +=1
#      if len(fibonacci_list)==100:
#            break
#print(fibonacci_list)
#2.yol
#fibonacci_list=list()
#fibonacci_list.append(1)
#fibonacci_list.append(1)
#for i in range(2,100):
#      fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
#print(fibonacci_list)
           
      
#100 basamaklı ilk fibonacci sayısını ekrana yazdıran program:

#fibonacci_list=list()
#fibonacci_list.append(1)
#fibonacci_list.append(1)
#index=2
#while True:
#      fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#      terim =fibonacci_list[index-2]+fibonacci_list[index-1]
#      if len(str(terim))==100:
#        print(terim)
#        print(index)
#        break
#      index+=1            


#1901 yılından 2000 yılına kadar kaç tane ayın ilk günğ pazar güne denk gelir?


#from datetime import datetime
#pazar_sayisi=0
#for yil in range(1901,2001):
#      for ay in range(1,13):
#            if datetime(yil,ay,1).weekday()==6:
#                  pazar_sayisi+=1
#print(pazar_sayisi)



#içinde çeşitli dosyalar olan bir klasörün içindeki dosyaları uzantılarına göre 
#farklı klasörlerde sınıflandırma:


#import os 

#def duzenle():
#      klasor=input("Düzenlenecek Klasör: ")
#      dosyalar=[] #dosyalar depolanacak
#      uzantilar=[] #uzantılar depolanacak
#      def list_dir():
#            for dosya in os.listdir(klasor):
#                  if os.path.isdir(os.path.join(klasor,dosya)): #dosyamız klasör mü? 
#                        continue
#                  if dosya.startswith("."): #dosyamız bir gizli dosya mı?
#                        continue
#                  else:
#                        dosyalar.append(dosya)
#      list_dir()
#      #Uzantıları alma
#      for dosya in dosyalar:
#            uzanti = dosya.split(".")[-1]
#            if uzanti in uzantilar: #uzantı daha önce eklendi mi
#                  continue
#            else:
#                  uzantilar.append(uzanti)
#      for uzanti in uzantilar: #klasörler oluşturuluyor
#            if os.path.isdir(os.path.join(klasor,uzanti)):
#                  continue
#            else:
#                  os.mkdir(os.path.join(klasor,uzanti))
#      for dosya in dosyalar:
#            uzanti=dosya.split(".")[-1]
#            os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))
#if __name__== "__main__" : #biz eğer herhangi bir modülü import edersek onun içinde açıkta bulunan çalıştırılabilir bir fonksiyon 
#  duzenle()               #varsa çalıştırılacaktı. eğer bunu yazmasaydım çalıştıracağı fonksiyonu hemen çalıştıracaktı. nbunu yazarak 
                          #eğer bu dosyanın kendisini çalıştırırsam çalışacaktır. 
                          
                          
                          
f = open ("deneme.txt","r")
icerik=f.read()
print(icerik)
f.close()
            
            
      
      




            
            

 


        