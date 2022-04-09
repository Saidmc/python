import time
import win32gui
import win32con

def ScreenOFF():
    """
    Function to turn off the screen.
    """
    return win32gui.SendMessage(win32con.HWND_BROADCAST,
                            win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def ScreenON():
    """
    Function to turn on the screen.
    """
    return win32gui.SendMessage(win32con.HWND_BROADCAST,
                            win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)

ScreenOFF()
time.sleep(3)
ScreenON()
