from backend.Financial_report import Financereport
from frontend.gui import Financeapp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = Financeapp(root)
    root.mainloop()