# Button Event Basic.py

from tkinter import *
import sys
from time import sleep

GUI = Tk()
GUI.geometry('300x600+20+50')

	

def click(evev):
	print('BUTTON CLICKED')
	Show.set("Click-button")
	


def EXIT(evan):
	Show.set("You double click Exit")
	print('You double click Exit')
	print('sleep-2')
	sleep(2) # หน่วงเวลา 2 วินาที
	sys.exit() #ออกจากโปรแกรม


Show = StringVar()
Show.set("Event")
sl = Label(GUI, text='display').pack()
show = Label(GUI,  textvariable = Show, borderwidth=2, relief="raised")
show.pack(ipadx= 120, ipady=20)
#Show.set(" ")
'''
If you want a border,
 the option is borderwidth.
  You can also choose the relief of the border:
   "flat", "raised", "sunken",
    "ridge", "solid", and "groove".
'''


myBtn = Button(GUI, text="BUTTON", command=click)
myBtn.bind("<Button-1>", click)#คลิกซ้าย
myBtn.pack(pady=20, ipadx=20, ipady=10)

EX = Button(GUI, text='EXIT', command=EXIT)
EX.pack(ipadx=25, ipady=10)
EX.bind("<Double-1>", EXIT) #ดับเบิ้ลคลิก


#myButton.bind("<Button-2>",  )#คลิกกลาง
#myButton.bind("<Button-3>") #คลิกขวา
#myButton.bind("<Enter>" )#เม้าชี้ทำงาน
#myButton.bind("<Leave>") #เม้าเลื่อนผ่านทำงาน



GUI.mainloop()
