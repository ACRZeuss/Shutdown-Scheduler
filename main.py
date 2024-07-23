import tkinter as tk
from tkinter import messagebox
import os
import platform
import time

def shutdown():
    try:
        # Süreyi al
        duration = int(entry.get())
        
        # Kullanıcıya doğrulama mesajı göster
        confirm = messagebox.askyesno("Onay", f"{duration} saniye içinde bilgisayar kapanacak. Onaylıyor musunuz?")
        
        if confirm:
            # Kullanıcının girdiği süreyi bekle
            time.sleep(duration)
            
            # İşletim sistemine göre kapatma komutunu çalıştır
            if platform.system() == "Windows":
                os.system("shutdown /s /t 1")
            elif platform.system() == "Linux" or platform.system() == "Darwin":
                os.system("shutdown -h now")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# Tkinter arayüzü oluştur
root = tk.Tk()
root.title("Bilgisayar Kapatma Zamanlayıcı")

# Süre giriş alanı
label = tk.Label(root, text="Kapatma süresi (saniye):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Kapatma butonu
button = tk.Button(root, text="Zamanlayıcıyı Başlat", command=shutdown)
button.pack(pady=20)

# Tkinter döngüsünü başlat
root.mainloop()
