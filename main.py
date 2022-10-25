import os
from random import randint, random
from time import sleep
import ayarlar
import düşmanlar
import oyuncu



temizle =lambda:os.system('cls')

def main():
    seçim = int(0)
    #bu kısım ana menu 
    temizle()
    print("savaş oyunu v0.0.0.2")
    print("1 oyuna başla")
    print("2 mevcut ayarlar")
    print("3 çıkış")
    seçim = int(input("seçimin = "))
    
    if int(seçim) >=4:
        print("geçersiz seçim")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return main()
    
    if int(seçim) == 1:
        temizle()
        print("yükleniyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        temizle()
        return oyun()
        
    if int(seçim) == 2:
        temizle()
        return ayar_ekranı()       
        
    if int(seçim) == 3:
        temizle()
        print("çıkılıyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        exit()
        
def ayar_ekranı():
    #burası ayar ekranı
    temizle()
    print("zorluk seviyesi=",int(ayarlar.ayarlar.zorluk_seviyesi))
    print("oyun hızı=",int(ayarlar.ayarlar.oyun_hızı))
    print("gym stat artışı =",int(ayarlar.ayarlar.gym_başına_gelen_stat_artışı))
    geridön=input("geri dönmek için her hangi bir tuşa gir")
    geridön= 0
    return main()




def oyun():
    seçim = int(0)
    #burası oyunun başladığı yer
    temizle()
    print("şehir meydanı")
    print("1 areneya gir ")
    print("2 GYM ye git ")
    print("3 karaketer özellikleri")
    print("4 menüye dön")
    seçim = int(input("seçimin = "))
    
    if int(seçim) >= 5:
        temizle()
        print("geçersiz seçim")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return oyun()
    if int(seçim) == 4:
        temizle()
        print("yükleniyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return main()
    if int(seçim) == 3:
        temizle()
        print("can=",int(oyuncu.statlar.oyuncu_canı))
        print("saldırı gücü=",int(oyuncu.statlar.oyuncu_saldırıgücü))
        print("savunma gücü=",int(oyuncu.statlar.oyuncu_savunma_gücü))
        print("şehir meydanına geri döncemk için herhangi bir tuşu girin basın")
        gidiş = input()
        return oyun()
    
    if int(seçim) == 2:
        #gym ye giriyosun statların artıyor
        temizle()
        print("GYM ye gidildi ve statları artı +",ayarlar.ayarlar.gym_başına_gelen_stat_artışı)
        oyuncu.statlar.oyuncu_saldırıgücü = oyuncu.statlar.oyuncu_saldırıgücü + ayarlar.ayarlar.gym_başına_gelen_stat_artışı
        oyuncu.statlar.oyuncu_canı= oyuncu.statlar.oyuncu_canı + ayarlar.ayarlar.gym_başına_gelen_stat_artışı
        oyuncu.statlar.oyuncu_savunma_gücü = oyuncu.statlar.oyuncu_savunma_gücü + ayarlar.ayarlar.gym_başına_gelen_stat_artışı
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return oyun()
    
    if int(seçim) == 1:
        temizle()
        print("savaş başlıyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        print("1")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        print("2")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        print("3")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return savaş()
        


def savaş():
    seçim = int(0)
    #arena menüsü alanı
    temizle()
    print("şu anki statların")
    print("can = ",int(oyuncu.statlar.oyuncu_canı))
    print("saldırı = ",int(oyuncu.statlar.oyuncu_saldırıgücü))
    print("savunma = ",int(oyuncu.statlar.oyuncu_savunma_gücü))
    print("arenaye girmeye eminmisin")
    print("1 evet")
    print("2 geri dön")
    seçim = int(input("seçimin = "))
    
    if int(seçim) == 1:
        return dövüş()
    
    if int(seçim) == 2:
        return oyun()
        
def dövüş():
    #rakibin seçilme yeri
    reset()
    temizle()
    rakip = randint(1,3)
    print("rakibin =",int(rakip))
    if int(rakip) == 1:
        temizle()
        print("rakibin barbar")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return barbar_dövüş()
    
    if int(rakip) == 2:
        temizle()
        print("rakibin goblin")
        sleep(ayarlar.ayarlar.oyun_hızı)
        return goblin_dövüş()
        
    
    if int(rakip) == 3:
        temizle()
        print("rakibin dövüşçü")
        sleep(ayarlar.ayarlar.oyun_hızı)
        return dövüşçü_dövüş()
    
    
def barbar_dövüş():
    #rakibin barbar ile dövüşüyorsun
    temizle()
    rakip_hamlesi = randint(1,2)#1 saldırma 2 iyileşme hamlesi
    
    print("rakibin canı",int(düşmanlar.barbar.can),"senin canın",int(oyuncu.statlar.oyuncu_canı))
    print("hamlen")
    print("1=saldır 2=iyileş 3 = savaçtan kaç")
    
    if int(düşmanlar.barbar.can) <= 0: # savaşı kazanma
        print("savaşı kazandın tebrikler arena menusune dönülüyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return savaş()
    
    if int(oyuncu.statlar.oyuncu_canı) <= 0:#hasteneye kaldırılma
        print("hastaneye kaldırılıyorsun ve +5 can alıyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(2)
        return oyun()
    
    senin_hamlen = int(input("senin hamlen = "))
   
    if int(senin_hamlen) >= 4:
        print("geçersiz seçenek")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return barbar_dövüş()
    
    
    if int(senin_hamlen) == 1: #saldırma hamlesi
        print("saldırıyorsun")
        düşmanlar.barbar.can = düşmanlar.barbar.can - oyuncu.statlar.oyuncu_saldırıgücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(senin_hamlen) == 2: #iyileşme hamlesi
        print("iyileşiyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(int(ayarlar.ayarlar.oyun_hızı))
    
    if int(senin_hamlen) == 3: #savaştan kaçma hamlesi
        print("savastan kaçıyorsun")
        return dövüş()
        
    #rakibin sırası
    
    if int(rakip_hamlesi) == 1:#rakip saldırıyor
        print("rakip saldırıyor")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı - düşmanlar.barbar.saldırı_gücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(rakip_hamlesi) == 2:#rakip iyileşiyor
        print("rakip iyileşiyor")
        düşmanlar.barbar.can = düşmanlar.barbar.can + 2
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
        
    return barbar_dövüş()


def goblin_dövüş():
    #rakibin goblin ile dövüşüyorsun
    temizle()
    rakip_hamlesi = randint(1,2)#1 saldırma 2 iyileşme hamlesi
    
    print("rakibin canı",int(düşmanlar.goblin.can),"senin canın",int(oyuncu.statlar.oyuncu_canı))
    print("hamlen")
    print("1=saldır 2=iyileş 3 = savaçtan kaç")
    
    if int(düşmanlar.goblin.can) <= 0: # savaşı kazanma
        print("savaşı kazandın tebrikler arena menusune dönülüyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return savaş()
    
    if int(oyuncu.statlar.oyuncu_canı) <= 0:#hasteneye kaldırılma
        print("hastaneye kaldırılıyorsun ve +5 can alıyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(2)
        return oyun()
    
    senin_hamlen = int(input("senin hamlen = "))
   
    if int(senin_hamlen) >= 4:
        print("geçersiz seçenek")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return barbar_dövüş()
    
    
    if int(senin_hamlen) == 1: #saldırma hamlesi
        print("saldırıyorsun")
        düşmanlar.goblin.can = düşmanlar.goblin.can - oyuncu.statlar.oyuncu_saldırıgücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(senin_hamlen) == 2: #iyileşme hamlesi
        print("iyileşiyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(int(ayarlar.ayarlar.oyun_hızı))
    
    if int(senin_hamlen) == 3: #savaştan kaçma hamlesi
        print("savastan kaçıyorsun")
        return dövüş()
        
    #rakibin sırası
    
    if int(rakip_hamlesi) == 1:#rakip saldırıyor
        print("rakip saldırıyor")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı - düşmanlar.goblin.saldırı_gücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(rakip_hamlesi) == 2:#rakip iyileşiyor
        print("rakip iyileşiyor")
        düşmanlar.goblin.can = düşmanlar.goblin.can + 2
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
        
    return goblin_dövüş()

def dövüşçü_dövüş():
    #rakibin goblin ile dövüşüyorsun
    temizle()
    rakip_hamlesi = randint(1,2)#1 saldırma 2 iyileşme hamlesi
    
    print("rakibin canı",int(düşmanlar.dövüşçü.can),"senin canın",int(oyuncu.statlar.oyuncu_canı))
    print("hamlen")
    print("1=saldır 2=iyileş 3 = savaçtan kaç")
    
    if int(düşmanlar.dövüşçü.can) <= 0: # savaşı kazanma
        print("savaşı kazandın tebrikler arena menusune dönülüyor")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return savaş()
    
    if int(oyuncu.statlar.oyuncu_canı) <= 0:#hasteneye kaldırılma
        print("hastaneye kaldırılıyorsun ve +5 can alıyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(2)
        return oyun()
    
    senin_hamlen = int(input("senin hamlen = "))
   
    if int(senin_hamlen) >= 4:
        print("geçersiz seçenek")
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        return barbar_dövüş()
    
    
    if int(senin_hamlen) == 1: #saldırma hamlesi
        print("saldırıyorsun")
        düşmanlar.dövüşçü.can = düşmanlar.dövüşçü.can - oyuncu.statlar.oyuncu_saldırıgücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(senin_hamlen) == 2: #iyileşme hamlesi
        print("iyileşiyorsun")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı + 5
        sleep(int(ayarlar.ayarlar.oyun_hızı))
    
    if int(senin_hamlen) == 3: #savaştan kaçma hamlesi
        print("savastan kaçıyorsun")
        return dövüş()
        
    #rakibin sırası
    
    if int(rakip_hamlesi) == 1:#rakip saldırıyor
        print("rakip saldırıyor")
        oyuncu.statlar.oyuncu_canı = oyuncu.statlar.oyuncu_canı - düşmanlar.dövüşçü.saldırı_gücü
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
    if int(rakip_hamlesi) == 2:#rakip iyileşiyor
        print("rakip iyileşiyor")
        düşmanlar.dövüşçü.can = düşmanlar.dövüşçü.can + 2
        sleep(int(ayarlar.ayarlar.oyun_hızı))
        
        
    return dövüşçü_dövüş()

def reset():
    düşmanlar.barbar.can = int(5)
    düşmanlar.barbar.saldırı_gücü = int(5)
    düşmanlar.barbar.savunma_gücü = int(1)
    
    düşmanlar.goblin.can = int(2)
    düşmanlar.goblin.saldırı_gücü = int(2)
    düşmanlar.goblin.savunma_gücü = int(1)
    
    düşmanlar.dövüşçü.can = int(5)
    düşmanlar.dövüşçü.saldırı_gücü = int(1)
    düşmanlar.dövüşçü.savunma_gücü = int(3)

    

main()