from link import *
import tkinter as tk
from tkinter import messagebox
import tkinter
window = tk.Tk()
window.title("Papermc server downloads")
window.geometry("400x400")
def show():
    print(f"1.19.2 : {mc1192}")
    print(f"1.19.1 : {mc1191}")
    print(f"1.19 : {mc119}")
    print(f"1.18.2 : {mc1182}")
    print(f"1.18.1 : {mc1181}")
    print(f"1.18 : {mc118}")
    print(f"1.17.1 : {mc1171}")
    print(f"1.17 : {mc117}")
    print(f"1.16.5 : {mc1165}")
    print(f"1.16.4 : {mc1164}")
    print(f"1.16.3 : {mc1163}")
    print(f"1.16.2 : {mc1162}")
    print(f"1.16.1 : {mc1161}")
    print(f"1.15.2 : {mc1152}")
    print(f"1.14.4 : {mc1144}")
    print(f"1.13.2 : {mc1132}")
    print(f"1.12.2 : {mc1122}")
    print(f"1.11.2 : {mc1122}")
    print(f"1.10.2 : {mc1102}")
    print(f"1.9.4 : {mc194}")
    print(f"1.8.8 : {mc188}")
#Button
btn = tk.Button(text="show")
btn.config(bg="skyblue")
btn.config(width=10,height=5)
btn.config(command=show)
btn.pack()
#end
window.mainloop()