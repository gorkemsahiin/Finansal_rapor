import psycopg2
import pandas as pd
import matplotlib.pyplot as plt 
from openpyxl import Workbook
import os

class Financereport:

    def __init__(self):
        try:
            
            self.conn = psycopg2.connect(
                dbname='finansal_rapor', 
                user='kullanici_model_owner', 
                password='ivjrteYVNs48', 
                host='ep-lively-block-a57av5fv-pooler.us-east-2.aws.neon.tech', 
                port='5432'
            )
            self.cursor = self.conn.cursor()
            print("Veritabanına başarıyla bağlanıldı.")
        except psycopg2.Error as e:
            print(f"Veritabanına bağlanırken hata oluştu: {e}")
            self.conn = None
            self.cursor = None

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS gelirler (
                id SERIAL PRIMARY KEY,
                miktar DECIMAL,
                aciklama TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS giderler (
                id SERIAL PRIMARY KEY,
                miktar DECIMAL,
                aciklama TEXT,
                kategori TEXT
            )
        """)
        self.conn.commit()

    def gelir_ekle(self, miktar, aciklama):
        self.cursor.execute("""
            INSERT INTO gelirler (miktar, aciklama) VALUES (%s, %s)
        """, (miktar, aciklama))
        self.conn.commit()

    def gider_ekle(self, miktar, aciklama, kategori):
        self.cursor.execute("""
            INSERT INTO giderler (miktar, aciklama, kategori) VALUES (%s, %s, %s)
        """, (miktar, aciklama, kategori))
        self.conn.commit()

    def raporla(self):
        self.cursor.execute("SELECT miktar, aciklama FROM gelirler")
        gelirler = self.cursor.fetchall()

        self.cursor.execute("SELECT miktar, aciklama, kategori FROM giderler")
        giderler = self.cursor.fetchall() 

        df_gelirler = pd.DataFrame(gelirler, columns=['Miktar', 'Açıklama'])
        df_giderler = pd.DataFrame(giderler, columns=['Miktar', 'Açıklama', 'Kategori'])

        toplam_gelir = df_gelirler['Miktar'].sum() if not df_gelirler.empty else 0
        toplam_gider = df_giderler['Miktar'].sum() if not df_giderler.empty else 0
        toplam_butce = toplam_gelir - toplam_gider

        plt.bar(['Gelir', 'Gider'], [toplam_gelir, toplam_gider], color=['#07c611', '#f70003'])
        plt.title('FİNANSAL GRAFİK CREATED BY:EKODER.APP')
        plt.ylabel('Miktar (₺)')
        plt.show()

        rapor = f"Toplam Gelir: {toplam_gelir} ₺\nToplam Gider: {toplam_gider} ₺\nToplam Bütçe: {toplam_butce} ₺"
        
        print("Gelirler Tablosu:")
        print(df_gelirler)
        
        print("Giderler Tablosu:")
        print(df_giderler)

        return rapor

    def get_data(self):
       try:
        self.cursor.execute("SELECT miktar, aciklama FROM gelirler")
        gelirler = self.cursor.fetchall()

        self.cursor.execute("SELECT miktar, aciklama, kategori FROM giderler")
        giderler = self.cursor.fetchall()

        return gelirler, giderler
       except Exception as e:
        print(f"Veri alınırken hata oluştu: {e}")
        return [], []  
    
    def save_to_excel(self):
        df_gelirler = pd.DataFrame(self.gelir_listesi, columns=['Miktar', 'Açıklama'])
        df_giderler = pd.DataFrame(self.gider_listesi, columns=['Miktar', 'Açıklama', 'Kategori'])

        with pd.ExcelWriter('finans_verileri.xlsx', engine='openpyxl', mode='w') as writer:
            df_gelirler.to_excel(writer, sheet_name='Gelirler', index=False)
            df_giderler.to_excel(writer, sheet_name='Giderler', index=False)

        os.system('start finans_verileri.xlsx')

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
