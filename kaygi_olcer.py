#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kaygı Ölçer v1.0
Bu program, kullanıcının varoluşsal kaygı seviyesini bilimsel olmayan ama son derece ciddi bir şekilde ölçer.
Dikkat: Sonuçlar %100 doğrudur. Bilim bunu onaylamıştır (hayal gücümde).
"""

import random
import time

def sor_soru(soru):
    print(f"\n{soru}")
    cevap = input("Cevabınız (1-10 arası): ")
    try:
        return int(cevap)
    except:
        return random.randint(1, 10)  # Yanlış girerse kader belirler

def main():
    print("=" * 50)
    print("   VAROLUŞSAL KAYGI ÖLÇER 3000")
    print("   'Neden buradayım?' sorusuna cevap arayanlar için")
    print("=" * 50)
    time.sleep(1)
    
    puan = 0
    
    sorular = [
        "Sabah uyandığında 'yine mi?' diye düşünme sıklığın?",
        "Boş bakışlarla tavana bakıp evrenin anlamsızlığını sorgulama süren (dakika)?",
        "İş/okul giderken 'asılında hiçbir şeyin önemi yok' hissi ne kadar güçlü?",
        "Kahve içerken 'bu kahve de boşuna' diye düşünme oranı?",
        "Gece 3'te uyanıp 'ben kimim?' sorusunu sorma eğilimin?"
    ]
    
    for soru in sorular:
        puan += sor_soru(soru)
        time.sleep(0.5)
    
    ortalama = puan / len(sorular)
    
    print("\n" + "=" * 50)
    print("SONUÇ HESAPLANIYOR...")
    time.sleep(2)
    print("Analiz tamamlandı. Kaderin belirlendi.")
    
    if ortalama < 3:
        mesaj = "Tebrikler! Sen ya gerçekten mutlusun ya da henüz uyanmadın. Varoluşsal kaygın yok denecek kadar az. Şüpheli."
    elif ortalama < 6:
        mesaj = "Orta seviye kaygı. Normal insan gibi yaşıyorsun. Biraz daha düşün, belki de yanılıyorsundur."
    elif ortalama < 8:
        mesaj = "Yüksek kaygı! Evren seni fark etmiş. Şimdi ya şiir yaz ya da çay demle."
    else:
        mesaj = "KRİTİK SEVİYE! Sen artık varoluşsal bir krizsin. Dünya sana yetmiyor. Hoş geldin, kulübe."
    
    print(f"\nKaygı Puanın: {ortalama:.1f}/10")
    print(mesaj)
    print("\nNot: Bu sonuç kesin ve değiştirilemezdir. İtiraz hakkın yoktur.")
    
    # Gizli not: bazen sistemin kendisi de sorgulanmalıdır, ama şimdilik bu kadar.
    # (saklı anlam: her şey kontrol altında gibi görünse de...)

if __name__ == "__main__":
    main()

# Damga: Bu kod 06.11.2026 tarihinde Kayyum Grok tarafından ciddiyetle (ve biraz da şakayla) yazılmıştır.
# İmza: K.G. - Varoluşun bekçisi
