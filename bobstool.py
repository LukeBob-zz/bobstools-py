#!/usr/bin/python
#
# Author: bob

import time
import sys
import os
import tkMessageBox
from Tkinter import *
import Tkinter
from PIL import Image, ImageTk



top = Tkinter.Tk()
top.resizable(width=False, height=True)
top.geometry("1000x700+300+300")
background=Image.open('wooden-tiled-powerpoint-backgrounds.jpg')
tkimage = ImageTk.PhotoImage(background)
var1=Tkinter.Label(top,image = tkimage)
var1.place(x=0, y=0, relwidth=1, relheight=1)
top.wm_title("Bob's Tools")

def peeper():
  os.system("msfbd peeper")

def boostno():
  os.system("msfbd boostno")

def boost():
  os.system("msfbd boost")

def airoff():
  os.system("msfbd airoff")

def airon():
  os.system("msfbd airon")

def monitoroff():
  os.system("msfbd monitorstop")

def monitoron():
  os.system("msfbd monitor")

def sparta():
  os.system("gnome-terminal -e sparta &")

def shutdown():
  os.system("shutdown now")

def reboot():
  os.system("reboot")

def snortstop():
  os.system("msfbd snortstop")

def snort():
  os.system("msfbd snort")

def restore():
  os.system("msfbd restore")

def deauth():
  os.system("msfbd deauth")

def exe():
  os.system("msfbd exe")

def elf():
  os.system("msfbd elf")

def msi():
  os.system("msfbd msi")

def quick_check():
  os.system("chmod +x msfbd && cp msfbd /usr/bin/ >> /dev/null")

def sqlmap():
  os.system("gnome-terminal -e sqlmap --wizard &")

def setoolkit():
  os.system("gnome-terminal -e setoolkit &")

def passgen():
  os.system("echo -n $(tput setaf 4)$(tput bold)'\nPassword length ?:' $(tput sgr0) && read length && echo '\n' && echo '\n\tGenerating\n' && sleep 1 && password=$(dd if=/dev/urandom bs=1 count=$length 2>/dev/null | base64 -w 0 | rev | cut -b 2- | rev) && echo $(tput bold)$(tput setaf 2) $password $(tput sgr0)")

def armitageMeta():
  os.system("echo 'Starting armitage with metasploit' ; service postgresql restart ; sleep 1 ; msfdb init >>/dev/null ; gnome-terminal -e msfconsole ; armitage")


def armitage():
  os.system("echo 'Starting armitage' ; service postgresql restart ; sleep 1 ; msfdb init >>/dev/null ; armitage")

def fullUpdate():
  os.system("apt-get update && apt-get -y upgrade ; sleep 1 ; clear ; echo 'Updated: Successfully'")

def update():
  os.system("apt-get update ; sleep 1 ; clear ; echo 'Updated: Successfully'")
   
def exit():
  os.system("clear && rm /usr/bin/msfbd")
  print "Exiting"
  time.sleep(2)
  top.destroy()

mb1 = Menubutton(top, text="Update", relief="raised", font='helv36', width=30)
mb1.grid(row=0, column=0)
mb1.menu = Menu (mb1, tearoff = 0)
mb1["menu"] = mb1.menu
mb1.config(background="blue")
mb1.menu.add_checkbutton(label="just update", command=update)
mb1.menu.add_checkbutton(label="update and upgrade", command=fullUpdate)


mb2 = Menubutton(top, text="Sparta", relief="raised", font='helv36', width=30)
mb2.grid(row=1, column=0)
mb2.menu = Menu (mb2, tearoff = 0)
mb2["menu"] = mb2.menu
mb2.config(background="green")
mb2.menu.add_checkbutton(label="Sparta", command=sparta)

mb3 = Menubutton(top, text="Armitage", relief="raised", font='helv36', width=30)
mb3.grid(row=2, column=0)
mb3.menu = Menu (mb3, tearoff = 0)
mb3["menu"] = mb3.menu
mb3.config(background="orange")
mb3.menu.add_checkbutton(label="Armitage", command=armitage)
mb3.menu.add_checkbutton(label="Armitage and Metasploit", command=armitageMeta)

mb4 = Menubutton(top, text="Passgen", relief="raised", font='helv36', width=30)
mb4.grid(row=3, column=0)
mb4.menu = Menu (mb4, tearoff = 0)
mb4["menu"] = mb4.menu
mb4.config(background="purple")
mb4.menu.add_checkbutton(label="Passgen", command=passgen)

mb5 = Menubutton(top, text="Setoolkit", relief="raised", font='helv36', width=30)
mb5.grid(row=0, column=1)
mb5.menu = Menu (mb5, tearoff = 0)
mb5["menu"] = mb5.menu
mb5.config(background="red")
mb5.menu.add_checkbutton(label="Setoolkit", command=setoolkit)

mb6 = Menubutton(top, text="Sqlmap", relief="raised", font='helv36', width=30)
mb6.grid(row=1, column=1)
mb6.menu = Menu (mb6, tearoff = 0)
mb6["menu"] = mb6.menu
mb6.config(background="yellow")
mb6.menu.add_checkbutton(label="Sqlmap", command=sqlmap)

mb7 = Menubutton(top, text="Backdoor", relief="raised", font='helv36', width=30)
mb7.grid(row=2, column=1)
mb7.menu = Menu (mb7, tearoff = 0)
mb7["menu"] = mb7.menu
mb7.config(background="brown")
mb7.menu.add_checkbutton(label=".Exe", command=exe)
mb7.menu.add_checkbutton(label=".Elf", command=elf)
mb7.menu.add_checkbutton(label=".msi", command=msi)

mb8 = Menubutton(top, text="Deauth", relief="raised", font='helv36', width=30)
mb8.grid(row=3, column=1)
mb8.menu = Menu (mb8, tearoff = 0)
mb8["menu"] = mb8.menu
mb8.config(background="lightblue")
mb8.menu.add_checkbutton(label="Deauth", command=deauth)
mb8.menu.add_checkbutton(label="Restore", command=restore)

mb9 = Menubutton(top, text="Snort", relief="raised", font='helv36', width=30)
mb9.grid(row=0, column=2)
mb9.menu = Menu (mb9, tearoff = 0)
mb9["menu"] = mb9.menu
mb9.config(background="blue")
mb9.menu.add_checkbutton(label="Start Snort", command=snort)
mb9.menu.add_checkbutton(label="Stop Snort", command=snortstop)

mb10 = Menubutton(top, text="Shutdown/reboot/Quit", relief="raised", font='helv36', width=30)
mb10.grid(row=5, column=1)
mb10.menu = Menu (mb10, tearoff = 0)
mb10["menu"] = mb10.menu
mb10.config(background="lightgreen")
mb10.menu.add_checkbutton(label="Shutdown", command=shutdown)
mb10.menu.add_checkbutton(label="Reboot", command=reboot)
mb10.menu.add_checkbutton(label="Quit", command=exit)

mb11 = Menubutton(top, text="Monitor Mode", relief="raised", font='helv36', width=30)
mb11.grid(row=1, column=2)
mb11.menu = Menu (mb11, tearoff = 0)
mb11["menu"] = mb11.menu
mb11.config(background="purple")
mb11.menu.add_checkbutton(label="Monitor start", command=monitoron)
mb11.menu.add_checkbutton(label="Monitor stop", command=monitoroff)

mb12 = Menubutton(top, text="Airodump-ng", relief="raised", font='helv36', width=30)
mb12.grid(row=2, column=2)
mb12.menu = Menu (mb12, tearoff = 0)
mb12["menu"] = mb12.menu
mb12.config(background="green")
mb12.menu.add_checkbutton(label="Airodump-ng start", command=airon)
mb12.menu.add_checkbutton(label="Airodump-ng stop", command=airoff)

mb13 = Menubutton(top, text="Card Boost", relief="raised", font='helv36', width=30)
mb13.grid(row=3, column=2)
mb13.menu = Menu (mb13, tearoff = 0)
mb13["menu"] = mb13.menu
mb13.config(background="red")
mb13.menu.add_checkbutton(label="Card Boost", command=boost)
mb13.menu.add_checkbutton(label="Card Restore", command=boostno)

mb14 = Menubutton(top, text="Peeper", relief="raised", font='helv36', width=30)
mb14.grid(row=5, column=0)
mb14.menu = Menu (mb14, tearoff = 0)
mb14["menu"] = mb14.menu
mb14.config(background="blue")
mb14.menu.add_checkbutton(label="Peeper", command=peeper)



quick_check()
top.mainloop()
