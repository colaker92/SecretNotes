import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import base64

# ---------------- ENCRYPTION / DECRYPTION ---------------- #

def encode(key, clear):
    encrypt = []
    for x in range(len(clear)):
        key_c = key[x % len(key)]
        enc_c = chr((ord(clear[x]) + ord(key_c)) % 256)
        encrypt.append(enc_c)
    return base64.urlsafe_b64encode("".join(encrypt).encode()).decode()

def decode(key, clear):
    decrypt = []
    # önce base64 çöz
    encrypted = base64.urlsafe_b64decode(clear.encode()).decode()
    # sonra key ile çözümle
    for x in range(len(encrypted)):
        key_c = key[x % len(key)]
        dec_c = chr((ord(encrypted[x]) - ord(key_c)) % 256)
        decrypt.append(dec_c)
    return "".join(decrypt)

# ---------------- SAVE & ENCRYPT ---------------- #

def save_and_encrypt_notes():
    title = title_entry.get().strip()
    message = secret_text.get("1.0", "end").strip()
    master_secret = master_entry.get().strip()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror("HATA ! ", "Başlık, Mesaj ya da Key kısmı boş bırakılamaz.!")
    else:
        message_encrypted = encode(master_secret, message)
        with open("secretnote.txt", "a") as data_file:
            data_file.write(f"\n{title}\n{message_encrypted}")
        # temizleme
        title_entry.delete(0, "end")
        secret_text.delete("1.0", "end")
        master_entry.delete(0, "end")

# ---------------- DECRYPT ---------------- #

def decrypt_notes():
    message_encrypted = secret_text.get("1.0", "end").strip()
    master_secret = master_entry.get().strip()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="HATA ! ", message="Mesaj veya Key kısmı boş bırakılamaz.! ")
    else:
        try:
            decrypted = decode(master_secret, message_encrypted)
            secret_text.delete("1.0", "end")
            secret_text.insert("1.0", decrypted)
        except Exception as e:
            messagebox.showerror("HATA !", f"Çözme sırasında hata oluştu: {e}")

# ---------------- TKINTER UI ---------------- #

window = tkinter.Tk()
window.title("Secret Notes")
window.config(bg="light gray", padx=50, pady=50)

# Görsel
topsecret_image = Image.open("topsecrettest.png")
resize = topsecret_image.resize((150, 150))
image = ImageTk.PhotoImage(resize)
image_label = tkinter.Label(window, image=image, bg="light gray", padx=50, pady=50)
image_label.pack()

# Başlık
title_label = tkinter.Label(window, text="Enter your title", bg="light gray", font=("Segoe UI", 15, "bold"))
title_label.pack()
title_entry = tkinter.Entry(window, width=40, font=("Segoe UI", 10))
title_entry.pack()

# Gizli Not
secret_label = tkinter.Label(window, text="Enter your secret", bg="light gray", font=("Segoe UI", 15, "bold"))
secret_label.pack()
secret_text = tkinter.Text(window, width=40, font=("Segoe UI", 10))
secret_text.pack()

# Master Key
master_label = tkinter.Label(window, text="Enter master key", bg="light gray", font=("Segoe UI", 15, "bold"))
master_label.pack()
master_entry = tkinter.Entry(window, width=40, font=("Segoe UI", 10))
master_entry.pack()

# Butonlar
encrypt_btn = tkinter.Button(window, text="Save & Encrypt", command=save_and_encrypt_notes, bg="red", fg="white", font=("Segoe UI", 8, "bold"), padx=5, pady=5)
encrypt_btn.pack(pady=4)

decrypt_btn = tkinter.Button(window, text="Decrypt", command=decrypt_notes,bg="green", fg="white", font=("Segoe UI", 8, "bold"), padx=5, pady=5)
decrypt_btn.pack(pady=4)

window.mainloop()