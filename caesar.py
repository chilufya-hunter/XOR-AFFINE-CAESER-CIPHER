

# мы будем использовать английский алфавит,и мы будем использовать функции, которые преобразуют 
# число в целые числа и целые числа в числа
A2Z = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
Z2A = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def caesar_encipher(originaltext, shift):
 
    # блок шифрования кода
    ciphertext = ""
    for c in originaltext.upper():
        if c.isalpha(): ciphertext += Z2A[ (A2Z[c] + shift)%26 ]
        else: ciphertext += c

    return ciphertext

def caesar_decipher(ciphertext, shift):
   
    # блок расшифровать код
    originaltext = ""
    for c in ciphertext.upper():
        if c.isalpha(): originaltext +=Z2A[(A2Z[c] - shift)%26 ]
        else: originaltext += c

    return originaltext
#импорт пакетов для построения приложения
import tkinter as tk
from tkinter import ttk

class encryption:

    def __init__(self, root):

        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.key = tk.IntVar(root)

        root.title("Шифра Цезаря")
       

        style = ttk.Style()
        style.configure("TLabel",
                        font = "Times 24 bold italic",
                        padding=16)
        style.configure("TButton",
                         font="Times 24 bold italic",
                         padding=16)
        style.configure("TEntry",
                        font="Times 24 bold italic",
                        padding=16)

        self.plain_label = tk.Label(root, text="оригинальный текст", fg="red", font="7").grid(row=1, column=0)

        self.plain_entry = ttk.Entry(root,
                                    textvariable=self.plain_text, width=50)
        self.plain_entry.grid(row=0, column=1, rowspan=4 , columnspan=4)

        self.plain_clear = tk.Button(root, text="удалить все",fg="red",font="7",
                                    command=lambda: self.clear('plain')).grid(row=2, column=0)

        self.key_label = tk.Label(root, text="сдвиг",font="7").grid(row=4, column=0)

        self.key_entry = ttk.Entry(root, textvariable=self.key).grid(row=4, column=1)

        self.encipher_button = ttk.Button(root, text=" шифрование ",
                                    command=lambda: self.encipher_press()).grid(row=4, column=3)

        self.decipher_button = ttk.Button(root, text="дешифрование ",
                                    command=lambda: self.decipher_press()).grid(row=4, column=4)

        self.cipher_label = tk.Label(root, text="Зашифрованный текст", fg="blue", font="7").grid(row=7, column=0)

        self.cipher_entry = ttk.Entry(root,
                                    textvariable=self.cipher_text, width=50)
        self.cipher_entry.grid(row=6, column=1, rowspan=4 , columnspan=4)

        self.cipher_clear = tk.Button(root, text="удфлить все",font="7",fg="blue",
                                    command=lambda: self.clear('шифрование')).grid(row=8, column=0)


    def clear(self, str_val):
        if str_val == 'шифрование':
            self.cipher_entry.delete(0, 'end')
        else:
            self.plain_entry.delete(0, 'end')

    def get_key(self):
        key_val = self.key.get()
        return key_val

    def encipher_press(self):
        key = self.get_key()
        cipher_text = caesar_encipher(self.plain_entry.get(), key)
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decipher_press(self):
        key = self.get_key()
        plain_text = caesar_decipher(self.cipher_entry.get(), key)
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)


root = tk.Tk()

caesar = encryption(root)

root.mainloop()
