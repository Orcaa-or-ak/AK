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
            #Vao game
            if (a == 0):
                try:
                    py.click('./img/findmatch.png')
                    a = 1
                except Exception:
                    pass
            if (a > 0):
                try:
                    py.click('./img/play.png')
                    a = 2
                except Exception:
                        pass

            #Trong game
            if (a == 2):
                #Roll
                if (b % 8 == 0):
                    try:
                        click(373,1035)
                    except Exception:
                        pass

                try: #1
                    py.moveTo('./img/champ/illaoi.png')
                    clickk()
                except Exception:
                    pass

                try: #2
                    py.moveTo('./img/champ/nami.png')
                    clickk()
                except Exception:
                    pass

                try: #3
                    py.moveTo('./img/champ/nidalee.png')
                    clickk()
                except Exception:
                    pass

                try: #4
                    py.moveTo('./img/champ/skarner.png')
                    clickk()
                except Exception:
                    pass

                try: #5
                    py.moveTo('./img/champ/varus.png')
                    clickk()
                except Exception:
                    pass

                try: #6
                    py.moveTo('./img/champ/vladimir.png')
                    clickk()
                except Exception:
                    pass

                try: #7
                    py.moveTo('./img/champ/senjuani.png')
                    clickk()
                except Exception:
                    pass

                try: #8
                    py.moveTo('./img/champ/ryze.png')
                    clickk()
                except Exception:
                    pass

                #Buy
                b = b + 1
                if (b % 10 == 0):
                    try:
                        py.moveTo('./img/exp.png')
                        clickk()
                    except Exception:
                        pass
                if (b % 5 == 0):
                    try:
                        click(373,1035)
                    except Exception:
                        pass


                #Thoat game
                try: 
                    py.moveTo('./img/exit.png')
                    clickk()
                    a = 0
                    b = 0
                    t.sleep(15)
                except Exception:
                    pass

            #Choi lai            
            try:
                py.click('./img/play_again.png')
                py.move(0,-50)  
            except Exception:
                pass
#======================================================
    lis.stop()


if __name__ == "__main__":
    main()