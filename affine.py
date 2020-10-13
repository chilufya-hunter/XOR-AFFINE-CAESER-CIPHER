
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# мы будем использовать английский алфавит,и мы будем использовать функции, которые преобразуют 
# число в целые числа и целые числа в числа
mn = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
nm = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def affine_encipher(plaintext, a, b):
    # блок шифрования кода
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += nm[ (mn[c] * a + b)%26 ]
        else: ciphertext += c

    return ciphertext

def affine_decipher(ciphertext, a, b):
   # блок расшифровать код
    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha(): plaintext += nm[ ( inv_a * (mn[c] - b) )%26 ]
        else: plaintext += c
    return plaintext

def validate_a(a):
    # чтобы найти обратную величину a
    inv_a = -1
    for x in range(1,26):
        if (a*x)%26 == 1:
            inv_a = x

    if inv_a == -1:
        # уведомление об ошибке
        messagebox.showerror("Ошибка", "'a' не имеет обратного значения , выберите другое значение для 'a'")
        raise ValueError("а не имеет обратной связи")


class encryption:

    def __init__(self, root):

        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.a = tk.IntVar(root)
        self.b = tk.IntVar(root)

        root.title("Аффинный Шифр")
       

        style = ttk.Style()
        style.configure("TLabel",
                        font = "Serif 15",
                        padding=10)
        style.configure("TButton",
                         font="Serif 15",
                         padding=10)
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.plain_label = tk.Label(root, text="оригинальный текст", fg="red", font="7",).grid(row=1, column=0)

        self.plain_entry = ttk.Entry(root,
                                    textvariable=self.plain_text, width=50)
        self.plain_entry.grid(row=0, column=1, rowspan=4 , columnspan=4)

        self.plain_clear = tk.Button(root, text="удалить все",fg="red", font="7",
                                    command=lambda: self.clear('plain')).grid(row=2, column=0)

        self.a_label = tk.Label(root, text="a").grid(row=4, column=0)

        self.a_entry = tk.Entry(root, textvariable=self.a).grid(row=4, column=1)

        self.b_label = tk.Label(root, text="b").grid(row=5, column=0)

        self.b_entry = tk.Entry(root, textvariable=self.b).grid(row=5, column=1)

        self.encipher_button = ttk.Button(root, text=" шифрование  ",
                                    command=lambda: self.encipher_press()).grid(row=4, column=3)

        self.decipher_button = ttk.Button(root, text=" дешифрование ",
                                    command=lambda: self.decipher_press()).grid(row=4, column=4)

        self.cipher_label = tk.Label(root, text="Зашифрованный текст", fg="blue", font="7",).grid(row=7, column=0)

        self.cipher_entry = ttk.Entry(root,
                                    textvariable=self.cipher_text, width=50)
        self.cipher_entry.grid(row=6, column=1, rowspan=4 , columnspan=4)

        self.cipher_clear = tk.Button(root, text="удалить все",fg="blue", font="7",
                                    command=lambda: self.clear('шифрование')).grid(row=8, column=0)



    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        else:
            self.plain_entry.delete(0, 'end')

    def get_key(self):
        a_val = self.a.get()
        validate_a(a_val)
        b_val = self.b.get()
        return a_val, b_val

    def encipher_press(self):
        a, b = self.get_key()
        cipher_text = affine_encipher(self.plain_entry.get(), a, b)
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decipher_press(self):
        a, b = self.get_key()
        plain_text = affine_decipher(self.cipher_entry.get(), a, b)
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)


root = tk.Tk()

caesar = encryption(root)

root.mainloop()
