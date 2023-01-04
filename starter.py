import tkinter as tk#load tk from tkinter
from tkinter import messagebox #load messagebox from tkinter
import os#load os
import time#load time
import threading#load threading
import configparser #load configparser
import webbrowser #load webbrowser
windows = tk.Tk()#windows is tk.Tk()
windows.title('Minecraft Server')#window title is Minecraft Server
windows.geometry('600x600')#window geometry is 600x600


#Fuction
def stop():#Fuction stop
    exit()#exit python
def version():#Fuction version
    messagebox.showinfo("version","You are using 3.0")#info text "You are using 3.0"
#end
def github():#Fuction github
    webbrowser.open("https://github.com/JaydenStudio/PY-Minecraft-Server")#open github
#Start
def start(): #Fuction start
    config = configparser.ConfigParser()
    config.read("config.ini")#read config.ini
    serverfile=os.path.exists("./Minecraft/server.jar")#True or False
    if serverfile==True: #if serverfile is True
        print("Server starts in 5 seconds")#print "Server starts in 5 seconds"
        time.sleep(5)#sleep 5 seconds
        os.system("cd Minecraft && java -jar server.jar")#Start server
        xx = os.path.isfile("./config.ini")#True or False
        if xx == True:#if xx is True
            try:
                Autorestart = config['config']['Autorestart']#read config
            except KeyError:
                with open("./config.ini","w",encoding="utf-8") as f:#write file
                    f.write("[config]\n")
                    f.write("Autorestart = True")
                    start()
            else:#if config is not empty
                Autorestart = config['config']['Autorestart']#read the config file
                if Autorestart == True or Autorestart == "true":#if Autorestart is True
                    start()#restart the server
                else:#if Autorestart is False
                    print("Server closed")#print Server closed
                    exit()#exit
        else:#if xx is False
            with open("./config.ini","w",encoding="utf-8") as f:#open the config file
                f.write("[config]\n")#write the config file
                f.write("Autorestart = True")#write the autorestart
                start()#restart the server
    else:#if serverfile is False
        print("Error: server.jar not found")#print "Error: server.jar not found"
#end
#run
def main():#Function main
    t1 = threading.Thread(target=start) #set target : start
    t1.start()#start server
    threading.enumerate()
#Button
btn = tk.Button(text="End")#Button text "End"
btn.config(bg="skyblue")#set button color "skyblue"
btn.config(width=10,height=5)#set button width "10" and height "5"
btn.config(command=stop)#set button command "stop"
btn.pack()
#end
#Button
btn = tk.Button(text="Start!")#Button text "Start"
btn.config(bg="skyblue")#set button color "skyblue"
btn.config(width=10,height=5)#set button width "10" and height "5"
btn.config(command=main)#set button command "main"
btn.pack()
#end
#Button
btn = tk.Button(text="version")
btn.config(bg="skyblue")#set button color "skyblue"
btn.config(width=10,height=5)#set button width "10" and height "5"
btn.config(command=version)#set button command "version"
btn.pack()
#end
#Button
btn = tk.Button(text="Github")
btn.config(bg="skyblue")#set button bg "skyblue"
btn.config(width=10,height=5)
btn.config(command=github)
btn.pack()
#end
messagebox.showinfo("Tips:","Use jdk17 or above")#messagebox info text "Use jdk17 or above"
b=os.path.exists("Minecraft")#True or False
if b==True:#if b is True
    print("INFO: Folder exists")#print "INFO: Folder exists"
    serverfile=os.path.exists("./Minecraft/server.jar")#True or False
    if serverfile==True:#if serverfile is True
        messagebox.showinfo("server","Successfully found server.jar")#messagebox info text "Successfully found server.jar"
    else:#if serverfile is False
        messagebox.showinfo("server","server.jar not found")#messagebox info text "server.jar not found"
else:#if b is False
    os.mkdir("Minecraft")#make directory "Minecraft"
    print("Folder Minecraft created successfully!")#print "Folder Minecraft created successfully!"
testfile=os.path.exists("./helloworld.jar")#True or False
if testfile==True:#if testfile is True
    os.system("java -jar helloworld.jar")#start test file
    os.system("echo If you see Hello world!,it means that your installed java successfully!")#print "If you see Hello world!,it means that your installed java successfully!"
else:#if testfile is False
    print("helloworld.jar not found")#print "helloworld.jar not found"


windows.mainloop()#loop