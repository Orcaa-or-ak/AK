#Pre:
#Tim tran: 833,939
#Choi luon: 961,786

#Ingame:
#Slot 1: 577,938
#Slot 2: 774,938
#Slot 3: 981,938
#Slot 4: 1175,938
#Slot 5: 1379,938

#After
#Choi lai: 833,939

import time as t
import win32api, win32con
import pyautogui as py
from pynput.keyboard import *

#  ======== settings ========
resume_key = Key.ctrl_r
pause_key = Key.alt_gr
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Controls:")
    print("\t Right CTRL = Resume")
    print("\t ALT GR (Right ALT)  = Pause")
    print("\t ESC = Exit")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def clickk():
    current = py.position()
    click(current[0],current[1])

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def rclickk():
    current = py.position()
    rclick(current[0],current[1])

def main():
    lis = Listener(on_press=on_press)
    lis.start()
    display_controls()
    a = 0
    b = 0
    while running:
        if not pause:
#======================================================   
            click(373,1035)
#======================================================
    lis.stop()


if __name__ == "__main__":
    main()