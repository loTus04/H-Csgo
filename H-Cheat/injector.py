import psutil
import win32gui
import win32con
import os
from pynput.keyboard import Listener
import time
import subprocess




# hide this console
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

#subprocess.Popen("start ./csgo_cheat.py")


consolOn = True

csgoOpen = False
while csgoOpen == False:
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "csgo.exe" in (p.info['name']).lower():
            csgoOpen = True

time.sleep(0.2)
cheat_hwnd = win32gui.FindWindow(None, "CSGO Hacks by Hawks and loTus04")
win32gui.SetWindowPos(cheat_hwnd, win32con.HWND_TOPMOST, 100, 100, 900, 550, 0)

# hide and show console when <DELET> is clicked
def on_press(key):
    key = str(key)
    key = key.replace("'", "")
    global consolOn

    if key == "9":
        exit()
    if key == "Key.delete":
        cheat_hwnd = win32gui.FindWindow(None, "CSGO Hacks by Hawks and loTus04")
        if consolOn == False:
            consolOn = True
            print(consolOn)
            win32gui.ShowWindow(cheat_hwnd, win32con.SW_SHOW)
        else:
            consolOn = False
            print(consolOn)
            win32gui.ShowWindow(cheat_hwnd, win32con.SW_HIDE)


with Listener(on_press=on_press) as listener:
    listener.join()