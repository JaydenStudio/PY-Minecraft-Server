import tkinter as tk
import os
import threading
window = tk.Tk()
window.geometry('200x200')
window.title("server")
#Function
def start_java():
    cmdline = "./"
    os.system(f"python {cmdline}starter.py")
#end
#Function
def start_bedrock():
    cmdline = "./"
    os.system(f"start {cmdline}pybserver/bedrock/mc/server.exe")
#end
#function
def main():
    t1 = threading.Thread(target=start_java)
    t1.start()
    print(threading.enumerate())
#end
#Function
def main2():
    t1 = threading.Thread(target=start_bedrock)
    t1.start()
    print(threading.enumerate())
#end
#Button
btn = tk.Button(text="start java server")
btn.config(bg="skyblue")
btn.config(width=15,height=5)
btn.config(command=main)
btn.pack()
#end
#Button
btn = tk.Button(text="start bedrock server")
btn.config(bg="skyblue")
btn.config(width=15,height=5)
btn.config(command=main2)
btn.pack()
#end
window.mainloop()