import tkinter as tk

class GelirView:
    def __init__(self, root):
        gelir_frame = tk.Frame(root)
        gelir_frame.grid(row=0, column=0, padx=20, pady=20)

        self.gelir_miktar_label = tk.Label(gelir_frame, text="Gelir Miktarı:")
        self.gelir_miktar_label.grid(row=0, column=0, pady=5)
        self.gelir_miktar_entry = tk.Entry(gelir_frame)
        self.gelir_miktar_entry.grid(row=0, column=1, pady=5)

        self.gelir_aciklama_label = tk.Label(gelir_frame, text="Gelir Açıklaması:")
        self.gelir_aciklama_label.grid(row=1, column=0, pady=5)
        self.gelir_aciklama_entry = tk.Entry(gelir_frame)
        self.gelir_aciklama_entry.grid(row=1, column=1, pady=5)

        self.gelir_ekle_button = tk.Button(gelir_frame, text="Gelir Ekle")
        self.gelir_ekle_button.grid(row=2, column=0, columnspan=2, pady=10)


class GiderView:
    def __init__(self, root):
        gider_frame = tk.Frame(root)
        gider_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        self.gider_miktar_label = tk.Label(gider_frame, text="Gider Miktarı:")
        self.gider_miktar_label.grid(row=0, column=0, pady=5)
        self.gider_miktar_entry = tk.Entry(gider_frame)
        self.gider_miktar_entry.grid(row=0, column=1, pady=5)

        self.gider_aciklama_label = tk.Label(gider_frame, text="Gider Açıklaması:")
        self.gider_aciklama_label.grid(row=1, column=0, pady=5)
        self.gider_aciklama_entry = tk.Entry(gider_frame)
        self.gider_aciklama_entry.grid(row=1, column=1, pady=5)

        self.gider_kategori_label = tk.Label(gider_frame, text="Gider Kategorisi:")
        self.gider_kategori_label.grid(row=2, column=0, pady=5)
        self.gider_kategori_entry = tk.Entry(gider_frame)
        self.gider_kategori_entry.grid(row=2, column=1, pady=5)

        self.gider_ekle_button = tk.Button(gider_frame, text="Gider Ekle")
        self.gider_ekle_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.raporla_button = tk.Button(gider_frame, text="Raporla")
        self.raporla_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="e")

        self.excel_button = tk.Button(gider_frame, text="Excel'e Aktar")  
        self.excel_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="e")  



def main():
    root = tk.Tk()
    root.geometry("600x400")
    

    gelir_view = GelirView(root)
    gider_view = GiderView(root)
    
   
    root.mainloop()


if __name__ == "__main__":
    main()
