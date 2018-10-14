#create msg.txt file in same folder 
#type all msg you wont to send seprated with ','
#open whatsapp web,open profile of reciver set cordinets in code and run code  :) done


import pyautogui 
import time
import random

pyautogui.FAILSAFE=True
time.sleep(4)

listmsg=[]
msg=[]


filepath='msg.txt'#give msg text file path 
with open(filepath,"r") as fp:
    para=fp.read()
    for i in para.strip().split(','):
   		listmsg.append(i) #two msg is splited by ,
    print(listmsg)


def sendmsg(msg):
	pyautogui.moveTo(900, 646) #cordinates are change heare
	pyautogui.click()
	print(msg)
	pyautogui.typewrite(msg)     
	pyautogui.press('enter') 
	g=random.uniform(0.5, 1.5)
	time.sleep(g)


for k in range(0,len(listmsg)):
	print(len(listmsg))
	for j in listmsg[k]:#type your message
		msg.append(j)
	sendmsg(msg)
	msg.clear()
