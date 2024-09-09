# gui_app.py

import tkinter as tk
from tkinter import messagebox
from encryption import encrypt
from deciphered import decrypt

def encrypt_text():
    text = entry_text.get()
    shift = entry_shift.get()
    
    if not text:
        messagebox.showerror("ERROR/1", "Enter The text!")
        return
    
    if not shift.isdigit():
        messagebox.showerror("ERROR/2", "Enter the key value (just number)!")
        return
    
    shift = int(shift)
    encrypted = encrypt(text, shift)
    encrypted_text.delete(1.0, tk.END)
    encrypted_text.insert(tk.END, encrypted)

def decrypt_text():
    text = encrypted_text.get(1.0, tk.END).strip()
    shift = entry_shift.get()
    
    if not text:
        messagebox.showerror("Hata", "Şifrelenmiş metin alanı boş olamaz!")
        return
    
    if not shift.isdigit():
        messagebox.showerror("Hata", "Anahtar geçerli bir sayı olmalıdır!")
        return
    
    shift = int(shift)
    decrypted = decrypt(text, shift)
    decrypted_text.delete(1.0, tk.END)
    decrypted_text.insert(tk.END, decrypted)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Caesar Cipher Uygulaması")

# Metin girişi için etiket ve giriş alanı
tk.Label(root, text="Metin:").grid(row=0, column=0)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1)

# Anahtar girişi için etiket ve giriş alanı
tk.Label(root, text="Anahtar:").grid(row=1, column=0)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1)

# Şifreleme ve deşifreleme butonları
encrypt_button = tk.Button(root, text="Şifrele", command=encrypt_text)
encrypt_button.grid(row=2, column=0)

decrypt_button = tk.Button(root, text="Deşifrele", command=decrypt_text)
decrypt_button.grid(row=2, column=1)

# Şifrelenmiş metin için metin alanı
tk.Label(root, text="Şifrelenmiş Metin:").grid(row=3, column=0)
encrypted_text = tk.Text(root, height=5, width=50)
encrypted_text.grid(row=3, column=1)

# Deşifrelenmiş metin için metin alanı
tk.Label(root, text="Deşifrelenmiş Metin:").grid(row=4, column=0)
decrypted_text = tk.Text(root, height=5, width=50)
decrypted_text.grid(row=4, column=1)

# Ana döngüyü başlat
root.mainloop()
