import telnetlib
import time
import os
hosts = "127.0.0.1"
ports = "25565" # default port
def main():
        try:
            telnetlib.Telnet(host=hosts, port=ports,timeout=2)
        except TimeoutError:
            print("Timeout")
        else:
            print("Connect")
inputport = input("server port (25565):")
if inputport == "" or inputport==25565:
    print("Your server port : 25565")
else:
    print(f"Your server port : {inputport} ")
    ports = inputport
inputhost = input("server host (localhost) : ")
if inputhost == "localhost" or inputhost == "127.0.0.1" or inputhost == "":
    print("Your server host : localhost")
else:
    print(f"Your server host : {inputhost}")
    hosts = inputhost
connections = input("Connections (5):")
if connections == "5" or connections == "":
    print("Connections : 5")
    connections = 5
else:
    print(f"Connections : {connections}")
for i in range(int(connections)):
    if(int(connections) >= 100):
     main()  
    else:
        time.sleep(1)
        main()
print("End connection")
os.system("pause")