import tkinter as tk
from frontend.views import GelirView, GiderView
from backend.controllers import FinansController
from frontend.styles import apply_styles 

class Financeapp:
    def __init__(self, root):
        self.gelir_view = GelirView(root)
        self.gider_view = GiderView(root)
        
   
        widgets = [self.gelir_view.gelir_miktar_label, self.gelir_view.gelir_miktar_entry,
                   self.gelir_view.gelir_aciklama_label, self.gelir_view.gelir_aciklama_entry,
                   self.gelir_view.gelir_ekle_button,
                   self.gider_view.gider_miktar_label, self.gider_view.gider_miktar_entry,
                   self.gider_view.gider_aciklama_label, self.gider_view.gider_aciklama_entry,
                   self.gider_view.gider_kategori_label, self.gider_view.gider_kategori_entry,
                   self.gider_view.gider_ekle_button, self.gider_view.raporla_button]
        
        for widget in widgets:
            apply_styles(widget)  
        
        self.controller = FinansController(self.gelir_view, self.gider_view)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  
    app = Financeapp(root)
    root.mainloop()
