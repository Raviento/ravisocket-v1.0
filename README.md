# WebSocket Komut Sunucusu

Bu proje, Python ile yazılmış şifre korumalı bir WebSocket sunucusu ve ona bağlanabilen modern, kullanıcı dostu bir istemci arayüzü içerir. Amaç, güvenli bir şekilde belirli komutları uzaktan çalıştırmak ve sonuçlarını anlık olarak görüntülemektir.

## Özellikler

- **Şifre Koruması:** Sunucuya bağlanmak için kullanıcıdan şifre istenir. Yanlış şifre girilirse bağlantı otomatik olarak kapatılır.
- **Komut Yetkilendirme:** Sadece belirlenen komutların çalıştırılmasına izin verilir. Güvenlik için komut listesi kolayca düzenlenebilir.
- **Komut Sonucu Gösterimi:** Girilen komutun çıktısı anında istemci arayüzünde görüntülenir.
- **Komut ve Sonuç Loglama:** Tüm komutlar ve çıktıları zaman damgası ile birlikte `log.txt` dosyasına kaydedilir.
- **Modern Web Arayüzü:** HTML ve CSS ile hazırlanmış, mobil uyumlu ve estetik bir istemci arayüzü.
- **Komut Geçmişi:** İstemci arayüzünde yukarı/aşağı ok tuşları ile önceki komutlara kolayca erişim.
- **Çoklu Cihaz Desteği:** Sunucu ayarları değiştirilerek farklı cihazlardan bağlantı sağlanabilir.

## Kullanım

### Sunucuyu Başlatmak

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install websockets
   ```
2. Sunucuyu başlatın:
   ```bash
   python server.py
   ```

### İstemciyi Kullanmak

1. `client.html` dosyasını bir tarayıcıda açın.
2. Sunucuya bağlanıldığında şifre girmeniz istenecek.
3. Şifreyi doğru girerseniz, izin verilen komutları gönderebilir ve sonuçlarını anlık olarak görebilirsiniz.

## Özelleştirme

- **Şifreyi Değiştirmek:**  
  `server.py` dosyasındaki `SIFRE` değişkenini güncelleyin.
- **İzinli Komutları Değiştirmek:**  
  `izinli_komutlar` listesine istediğiniz komutları ekleyin veya çıkarın.
- **Sunucuya Farklı Cihazlardan Erişim:**  
  `server.py` içindeki `host="localhost"` kısmını `host="0.0.0.0"` olarak değiştirin.

## Güvenlik Uyarısı

Bu uygulama sadece belirli komutlara izin verse de, komut çalıştırma işlemleri potansiyel riskler taşır. Sunucuyu güvenli bir ağda ve güvenilir kullanıcılarla kullanmanız önerilir.

## Dosya Yapısı

- `server.py` : WebSocket sunucu kodu
- `client.html` : Web istemcisi arayüzü
- `log.txt` : Komut ve sonuçların kaydedildiği dosya

---

**Hazırlayan:**  
Raviento