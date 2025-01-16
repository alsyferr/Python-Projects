from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

#brightness
import screen_brightness_control as pct

#audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#clock
from time import strftime

#calendar
from tkcalendar import *

#open google
import pyautogui

import subprocess
import webbrowser as wb
import random

root=Tk()
root.title('mac-soft Tool')
root.geometry("850x500+300+170")
root.resizable(False,False)
root.configure(bg='#292e2e')

#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Body=Frame(root,width=900,height=600,bg="#d6d6d6")
Body.pack(pady=20,padx=20)

#-------------------------------------------------
LHS=Frame(Body,width=310,height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHS.place(x=10,y=10)

#logo
photo=PhotoImage(file="Image/laptop.png")
myimage=Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=2,y=20)

my_system=platform.uname()
l1=Label(LHS, text=my_system.node,bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l1.place(x=20,y=200)

l2=Label(LHS, text=f"Version:{my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept",8),justify="center")
l2.place(x=20,y=225)

l3=Label(LHS, text=f"System:{my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l3.place(x=20,y=250)

l4=Label(LHS, text=f"Machine:{my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l4.place(x=20,y=285)

l5=Label(LHS, text=f"Total RAM installed:{round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l5.place(x=20,y=310)

l6=Label(LHS, text=f"Processor:{my_system.processor}",bg="#f4f5f5",font=("Acumin Variable Concept",7,'bold'),justify="center")
l6.place(x=20,y=340)


#-------------------------------------------------
RHS=Frame(Body,width=470,height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHS.place(x=330,y=10)

system=Label(RHS, text='System',font=("Acumin Variable Concept",15),bg="#f4f5f5")
system.place(x=10,y=10)


#######################Battery###################################################

def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours,minutes,seconds)

def none():
    global battery_png
    global battery_label
    
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)
    
    lb1.config(text=f"{percent}%")
    lb1_plug.config(text=f'Plug in:{str(battery.power_plugged)}')
    lb1_time.config(text=f'{time} remaining')
    
    battery_label=Label(RHS,background='#f4f5f5')
    battery_label.place(x=15,y=50)
    
    lb1.after(1000,none)
    
    if battery.power_plugged==True:
        battery_png=PhotoImage(file="Image/charging.png")
        battery_label.config(image=battery_png)
        
    else:
        battery_png=PhotoImage(file='Image/battery.png')
        battery_label.config(image=battery_png)

lb1=Label(RHS,font=("Acumin Variable Concept",40,'bold'),bg='#f4f5f5')
lb1.place(x=200,y=40)

lb1_plug=Label(RHS,font=("Acumin Variable Concept",10),bg='#f4f5f5')
lb1_plug.place(x=20,y=100)

lb1_time=Label(RHS,font=("Acumin Variable Concept",15),bg='#f4f5f5')
lb1_time.place(x=200,y=100)

none()


#################################################################################




#######################Speaker###################################################


lb1_speaker=Label(RHS,text="Speaker:",font=('arial',10,'bold'),bg="#f4f5f5")
lb1_speaker.place(x=10,y=150)
volume_value=tk.DoubleVar()

def get_current_volume_value():
    return '{: 2f}'.format(volume_value.get())

def volume_changed(event):
    device=AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()),None)
    
style=ttk.Style()
style.configure("Tscale", background='#f4f5f5')

volume=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',command=volume_changed,variable=volume_value)

volume.place(x=90,y=150)
volume.set(20)




#################################################################################



#######################Brightness###################################################


lb1_brightness=Label(RHS,text='Brightness',font=('arial',10,'bold'),bg="#f4f5f5")
lb1_brightness.place(x=10,y=190)

current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())

brightness= ttk.Scale(RHS,from_=0,to=100,orient='horizontal',command=brightness_changed,variable=current_value)
brightness.place(x=90,y=190)


#################################################################################

def weather():
    app1=Toplevel()
    app1.geometry('850x500+300+170')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)
    
    #icon
    image_icon=PhotoImage(file='Image/App1.png')
    app1.iconphoto(False,image_icon)
    
    #search box
    Search_image=PhotoImage(file="Image/search.png")
    myimage=Label(app1,image=Search_image,bg="#f4f5f5")
    myimage.place(x=20,y=20)
    
    textfield=tk.Entry(app1,justify='center',width=17,font=('poppins',25,'bold'),bg='#404044',border=0,fg="white")
    textfield.place(x=50,y=40)
    textfield.focus()
    
    Search_icon=PhotoImage(file="Image/search_icon.png")
    myimage_icon=Button(app1,image=Search_icon,borderwidth=0,cursor='hand2',bg="#404040")
    myimage_icon.place(x=400,y=34)
    
    #logo
    Logo_image=PhotoImage(file="Image/box.png")
    
    
    app1.mainloop()






#-------------------------------------------------
RHB=Frame(Body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHB.place(x=330,y=255)

apps=Label(RHB,text='Apps',font=('Acumin Variable Concept',15),bg='#f4f5f5')
apps.place(x=10,y=10)

app1_image=PhotoImage(file='Image/App1.png')
app1=Button(RHB,image=app1_image,bd=0,command=weather)
app1.place(x=15,y=50)

app2_image=PhotoImage(file='Image/App2.png')
app2=Button(RHB,image=app2_image,bd=0)
app2.place(x=100,y=50)

app3_image=PhotoImage(file='Image/App3.png')
app3=Button(RHB,image=app3_image,bd=0)
app3.place(x=185,y=50)

app4_image=PhotoImage(file='Image/App4.png')
app4=Button(RHB,image=app4_image,bd=0)
app4.place(x=270,y=50)

app5_image=PhotoImage(file='Image/App5.png')
app5=Button(RHB,image=app5_image,bd=0)
app5.place(x=355,y=50)

app6_image=PhotoImage(file='Image/App6.png')
app6=Button(RHB,image=app6_image,bd=0)
app6.place(x=15,y=120)

app7_image=PhotoImage(file='Image/App7.png')
app7=Button(RHB,image=app7_image,bd=0)
app7.place(x=100,y=120)

app8_image=PhotoImage(file='Image/App8.png')
app8=Button(RHB,image=app8_image,bd=0)
app8.place(x=185,y=120)

app9_image=PhotoImage(file='Image/App9.png')
app9=Button(RHB,image=app9_image,bd=0)
app9.place(x=270,y=120)

app10_image=PhotoImage(file='Image/App10.png')
app10=Button(RHB,image=app10_image,bd=0)
app10.place(x=355,y=120)


root.mainloop()