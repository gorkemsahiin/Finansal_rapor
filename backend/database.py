import psycopg2

class Database:
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
            print("Veritabanına bağlantı başarılı.")
        except psycopg2.Error as e:
            print(f"Veritabanına bağlanırken hata oluştu: {e}")
            self.conn = None
            self.cursor = None

    def close(self):
        
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        print("Bağlantı kapatıldı.")
