# Telefon Rehberi Uygulaması

Bu proje, FastAPI ve SQLAlchemy ile geliştirilmiş bir telefon rehberi API uygulamasıdır. Veritabanı olarak Microsoft SQL Server kullanılarak rehbere kişi ekleme, silme, düzenleme, görüntüleme ve kişi arama işlemlerini gerçekleştirir. 

## İçindekiler
- [Dosya Organizasyonu](#dosya-organizasyonu)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Veritabanı Şeması](#veritabanı-şeması)
- [Kullanımı](#api-kullanımı)
- [Örnek Kullanım](#örnek-kullanım)

## Dosya Organizasyonu

Proje dosyalarının organizasyonu ve aralarındaki ilişkiler aşağıdaki gibidir:

```bash
📁 rehber-api
│
├── README.md              # Proje hakkında genel bilgiler, kullanım ve kurulum talimatları
├── __init__.py            # Paket yapılandırma dosyası
├── database.py            # Veritabanı bağlantısı ve oturum yönetimi
├── main.py                # FastAPI uygulamasının ana dosyası ve uç nokta tanımlamaları
├── models.py              # SQLAlchemy modellerini tanımlar
├── schemas.py             # Pydantic şemalarını tanımlar
└── requirements.txt       # Projede kullanılan kütüphaneleri tanımlar
```


## Özellikler

- **Kişi ekle**: İsim, soyisim, telefon numarası ve adres gibi bilgileri veritabanına ekler.
- **Kişileri listele**: Tüm kayıtlı kişilerin bilgilerini döndürür.
- **Kişiyi ID ile arama**: Belirli bir ID'ye sahip kişiyi arar.
- **Kişiyi düzenle**: Id ile mevcut bir kişinin bilgilerini günceller.
- **Kişiyi sil**:Id ile rehberden bir kişiyi siler.




### Gereksinimler
- Python 3.x
- Microsoft SQL Server ve ODBC sürücüsü (ODBC Driver 17 for SQL Server)
- Python için `FastAPI`, `SQLAlchemy`, `pyodbc`, ve `uvicorn` paketleri


## Kurulum

1. Proje bağımlılıklarını yükleyin:
   pip install -r requirements.txt

2. `database.py` dosyasındaki veritabanı bağlantı ayarlarını düzenleyin:
   server_name = "SUNUCU_ADINIZ"  # SQL Server ismi
   database_name = "telefon_rehberi"  # Veritabanı adı

3. Veritabanı tablolarını oluşturmak için `main.py` kodunu çalıştırarak FastAPI'yi başlatın:
   uvicorn rehber.main:app --reload


## Veritabanı Şeması
- Kişi bilgilerinin saklandığı "rehber" tablosu:
- ![image](https://github.com/user-attachments/assets/bd8ae248-c192-42ee-a9e2-00bd0b57dd69)
- Bu tablo eğer mevcut değilse, uygulama çalıştığında otomatik olarak oluşturulur.

## Kullanım
FastAPI ile aşağıdaki uç noktaları kullanarak rehberde işlem yapabilirsiniz.

### Uç Noktalar

1. **Kişi Ekle**
   - **URL:** `/rehber`
   - **Metot:** `POST`
   - **Parametreler:** `Name`, `Surname`, `Number`, `Adress`
   - **Yanıt:** Eklenen kişinin bilgileri

2. **Kişileri Listele**
   - **URL:** `/rehber`
   - **Metot:** `GET`
   - **Yanıt:** Tüm kayıtlı kişilerin bilgileri

3. **Kişi Ara**
   - **URL:** `/rehber/{id}`
   - **Metot:** `GET`
   - **Parametreler:** `id` (aranacak kişinin ID'si)
   - **Yanıt:** Belirli kişiye ait bilgiler

4. **Kişi Sil**
   - **URL:** `/rehber/{id}`
   - **Metot:** `DELETE`
   - **Parametreler:** `id` (silinecek kişinin ID'si)
   - **Yanıt:** Başarı durumunda `"detail": "Kişi silindi"` mesajı

5. **Kişi Güncelle**
   - **URL:** `/rehber/{id}`
   - **Metot:** `PUT`
   - **Parametreler:** `id` (güncellenecek kişinin ID'si), `Name`, `Surname`, `Number`, `Adress`
   - **Yanıt:** Güncellenen kişinin bilgileri

### Örnek Kullanım

**Yeni bir kişi eklemek için:**
1. `/rehber` URL'ine `POST` isteği gönderin.
2. İstek gövdesine aşağıdaki gibi bir JSON nesnesi ekleyin:
   ```json
   {
       "Name": "Ahmet",
       "Surname": "Yılmaz",
       "Number": "05551234567",
       "Adress": "İstanbul"
   }


```
 ### örnek
Yeni bir kişi eklemek için:
- Menüden 1 numaralı seçeneği seçin.
- Kişinin bilgilerini (İsim, Soyisim, Telefon Numarası, Adres) girin.
- Uygulama, kişiyi eklediğinizi doğrular.
 



























    
