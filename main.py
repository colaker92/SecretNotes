import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk



# PENCERE

window = tkinter.Tk()
window.title("Secret Notes")
window.config(bg="light gray")
window.minsize(800,600)
window.config(padx=50, pady=50)


# FUNCTION

def encrypyMessage():
    print("click")

def decryptMessage():
    print("clicked")

# IMAGE

topsecret_image = Image.open("topsecrettest.png")
resize = topsecret_image.resize((150,150))

image = ImageTk.PhotoImage(resize)
image_label = tkinter.Label(window, image=image, padx=50, pady=50)
image_label.config(bg="light gray")
image_label.pack()


title_label = tkinter.Label(window, text="Enter your title")
title_label.config(bg="light gray", font=("Segoe UI", 15, "bold"))
title_label.pack()
title_entry = tkinter.Entry(window, width=40, font=("Segoe UI", 10))
title_entry.pack()

secret_label = tkinter.Label(window, text="Enter your secret")
secret_label.config(bg="light gray", font=("Segoe UI", 15, "bold"))
secret_label.pack()
secret_text = tkinter.Text(window, width=40, font=("Segoe UI", 10))
secret_text.pack()

master_label = tkinter.Label(window, text="Enter your master")
master_label.config(bg="light gray", font=("Segoe UI", 15, "bold"))
master_label.pack()
master_entry = tkinter.Entry(window, width=40, font=("Segoe UI", 10))
master_entry.pack()

encrypt_btn = tkinter.Button(window,text="Save & Encrypt")
encrypt_btn.config(bg="red", fg="white",command=encrypyMessage ,font=("Segoe UI", 8, "bold"))
encrypt_btn.config(padx=5, pady=5)
encrypt_btn.pack(pady=4)

decrypt_btn = tkinter.Button(window,text="Decrypt")
decrypt_btn.config(bg="green",fg="white",command=decryptMessage ,font=("Segoe UI", 8, "bold"))
decrypt_btn.config(padx=5, pady=5)
decrypt_btn.pack(pady=4)



window.mainloop()

#bu projede Decrypt kullanılacak sanırım
# tkinter.messagebox aratılacak bakılacak ve kullanılacak
# Görsel koymayı araştır onuda ekle projeye
#  Encrypt - Decrypt - cryptlogy googledan araştırıp stackowerflow dan kopyala yapıştır yapabiliriz
# Herşeyi fonksiyona bağlamayı unutma



