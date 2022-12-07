import tkinter as tk
import os
import time
import threading
windows = tk.Tk()
windows.title('Minecraft Server')
windows.geometry('600x600')


#Fuction
def stop():
    exit()
#end
#Start
def start():
    os.system(".\mc\server.exe")
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
btn.config(command=stop)
btn.pack()
#end
#Button
btn = tk.Button(text="Start!")
btn.config(bg="skyblue")
btn.config(width=10,height=5)
btn.config(command=main)
btn.pack()


windows.mainloop()