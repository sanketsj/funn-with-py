import pyautogui 
import time
import random
pyautogui.FAILSAFE = True
time.sleep(5)
for i in range(0,500):#how many times you wont to send
	pyautogui.moveTo(900, 646) #cordinates are change heare
	pyautogui.click()
	pyautogui.typewrite(['h','a','p','p','y',' ','b','i','r','t','h','d','a','y']) #msg what you wont to send your bee    
	pyautogui.press('enter') 
	g=random.uniform(0, 0.9)
	print(g)
	time.sleep(g)

