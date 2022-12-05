import tkinter as tk
from tkinter import messagebox
import os
import time
import threading
windows = tk.Tk()
windows.title('Minecraft Server')
windows.geometry('600x600')


#Fuction
def end():
    exit()
#end
#Start
def start():
    serverfile=os.path.exists("./Minecraft/server.jar")
    if serverfile==True:
        print("Server starts in 5 seconds")
        time.sleep(5)
        os.system("cd Minecraft && java -jar server.jar")
        print("Server closed")
    else:
        print("Error: server.jar not found")
#end
#run
def main():
    t1 = threading.Thread(target=start)
    t1.start()
    print(threading.enumerate())
#Button
btn = tk.Button(text="End")
btn.config(bg="skyblue")
btn.config(width=10,height=5)
btn.config(command=end)
btn.pack()
#end
#Button
btn = tk.Button(text="Start!")
btn.config(bg="skyblue")
btn.config(width=10,height=5)
btn.config(command=main)
btn.pack()
#end
messagebox.showinfo("Tips:","Use jdk17 or above")
a=os.path.exists("log")
if a==True:
    print("INFO: Folder exists")
else:
    os.mkdir("log")
    print("Folder log created successfully!")
b=os.path.exists("Minecraft")
if b==True:
    print("INFO: Folder exists")
    serverfile=os.path.exists("./Minecraft/server.jar")
    if serverfile==True:
        messagebox.showinfo("server","Successfully found server.jar")
    else:
        messagebox.showinfo("server","server.jar not found")
else:
    os.mkdir("Minecraft")
    print("Folder Minecraft created successfully!")
testfile=os.path.exists("./helloworld.jar")
if testfile==True:
    os.system("java -jar helloworld.jar")
    os.system("echo If you see Hello world!,it means that your installed java successfully!")
else:
    print("helloworld.jar not found")


windows.mainloop()