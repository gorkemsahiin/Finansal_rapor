# Finansal Rapor Projesi

Finansal Rapor Projesi, gelir ve giderlerinizi takip etmenize, bütçenizi hesaplamanıza ve finansal verilerinizi kullanıcı dostu bir arayüz ile yönetmenize olanak tanır.

## Özellikler
- Gelir ve gider ekleme
- Toplam bütçe hesaplama
- Gelir ve gider raporlaması
- Veritabanında gelir ve giderlerin saklanması
- Kullanıcı dostu Tkinter arayüzü

## Gereksinimler
- Python 3.x
- PostgreSQL (Neon Console veya yerel PostgreSQL sunucusu)
- Gerekli Python kütüphaneleri:
  - `psycopg2`
  - `pandas`
  - `matplotlib`
  - `tkinter` (Python'un standart kütüphanesi ile gelir)

## Kurulum
1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/gorkemsahiin/Finansal_rapor.git
## Gerekli kütüphaneleri yükleyin:

'''bash
pip install psycopg2 pandas matplotlib

## Veritabanı bağlantısını yapılandırın: finans.py dosyasında PostgreSQL veritabanı URL'inizi güncelleyin.

## Veritabanı tablolarını oluşturun: Veritabanına bağlanarak gelirler ve giderler tablolarını oluşturun. Bu adım, Finansraporu sınıfının _create_tables metoduyla otomatik olarak yapılacaktır.

## Kullanım
Gelir ekle: Gelir miktarı ve açıklamasını girin.
Gider ekle: Gider miktarı, açıklaması ve kategorisini girin.
Raporlama: Gelir, gider ve toplam bütçenizi görüntüleyin.
Veritabanı sorguları: PostgreSQL veritabanınızda veri sorgulamak için SQL komutlarını çalıştırın.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.

