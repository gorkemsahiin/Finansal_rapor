from tkinter import messagebox
from backend.Financial_report import Financereport
import pandas as pd  
import os

class FinansController:
    def __init__(self, gelir_view, gider_view):
        self.finans = Financereport()
        self.gelir_view = gelir_view
        self.gider_view = gider_view

        self.gelir_view.gelir_ekle_button.config(command=self.gelir_ekle)
        self.gider_view.gider_ekle_button.config(command=self.gider_ekle)
        self.gider_view.raporla_button.config(command=self.raporla)
        self.gider_view.excel_button.config(command=self.export_excel)  

    def gelir_ekle(self):
        try:
            miktar = float(self.gelir_view.gelir_miktar_entry.get())
            aciklama = self.gelir_view.gelir_aciklama_entry.get()
            if aciklama:
                self.finans.gelir_ekle(miktar, aciklama)
                messagebox.showinfo("Gelir Eklendi", f"Gelir eklendi: {miktar} ₺  - {aciklama}")
        except ValueError:
            messagebox.showwarning("UYARI", "Geçerli bir miktar giriniz")

    def gider_ekle(self):
        try:
            miktar = float(self.gider_view.gider_miktar_entry.get())
            aciklama = self.gider_view.gider_aciklama_entry.get()
            kategori = self.gider_view.gider_kategori_entry.get()
            if aciklama and kategori:
                self.finans.gider_ekle(miktar, aciklama, kategori)
                messagebox.showinfo("Gider Eklendi", f"Gider Eklendi: {miktar} ₺ - {aciklama} - {kategori}")
            else:
                messagebox.showwarning("UYARI", "Gider açıklaması ve kategorisi boş bırakılamaz")
        except ValueError:
            messagebox.showwarning("UYARI", "Geçerli bir miktar giriniz")

    def export_excel(self):
        gelirler, giderler = self.finans.get_data()

        gelir_data = {
            " Gelir Miktarı": [gelir[0] for gelir in gelirler],
            " Açıklama": [gelir[1] for gelir in gelirler]
        }
        gelir_df = pd.DataFrame(gelir_data)

        gider_data = {
            " Gider Miktarı": [gider[0] for gider in giderler],
            " Açıklama": [gider[1] for gider in giderler],
            " Kategori": [gider[2] for gider in giderler]
        }
        gider_df = pd.DataFrame(gider_data)
        excel_path = "rapor.xlsx"
        with pd.ExcelWriter("rapor.xlsx", engine='openpyxl', mode='w') as writer:
            gelir_df.to_excel(writer, sheet_name='Gelirler', index=False)
            gider_df.to_excel(writer, sheet_name='Giderler', index=False)

        messagebox.showinfo("Başarılı", "Veriler Excel dosyasına aktarıldı!")

        os.startfile(excel_path)

    def raporla(self):
        rapor = self.finans.raporla()
        messagebox.showinfo("Bütçe Raporu", rapor)
