import tkinter as tk
import os
import ImgConverter
from tkinter.filedialog import askopenfilename

Root = tk.Tk()
Root.title("Text Detector")
Root.geometry('1000x600')


def Upload():
    file = askopenfilename(defaultextension=".txt", filetypes=[
        ("JPEG", ".jpeg"), ("JPG", ".jpg"), ("PNG", ".png"), ("All Files", "*.*")])
    Current_path = os.path.abspath(file)
    print(ImgConverter.ConvertText(Current_path))
    inputtxt.insert(1.0, ImgConverter.ConvertText(Current_path))


inputtxt = tk.Text(Root, height=30, width=100)
inputtxt.pack()

printButton = tk.Button(Root, text='Upload an Image Here', command=Upload)
printButton.pack(ipadx=5, ipady=5, pady=30)

Root.mainloop()