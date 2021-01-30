from Cos.Cos64 import Kernel
from Cos.Cos64 import CrashHandler
import keyboard
import time

running = True
toggle = True


def Toggle():
    global toggle
    toggle = False
    print("hotkey input")


def Hotkeys():
    while toggle:
        SystemHotkeys()


def SystemHotkeys():
    global toggle
    if keyboard.is_pressed("f8"):
        print("Kernel running " + str(Kernel.running))
        time.sleep(0.5)

    if keyboard.is_pressed("f3"):
        CrashHandler.CrashHandler("User_Started_Screen_Of_Death", True)

    if keyboard.is_pressed("f4"):
        Kernel.Prepare_For_shutdown()
        Kernel.Shutdown()

    if keyboard.is_pressed("f5"):
        try:
            Doc = open("Cos/doc.txt", "r")
            Doc_Contents = Doc.read()
            print(Doc_Contents)
            Doc.close()

        except FileExistsError:
            print("Could not find file")
        time.sleep(0.5)

    if keyboard.is_pressed("f2"):
        if toggle:
            toggle = False
            print("hotkey input")
            time.sleep(0.5)

        if not toggle:
            toggle = True
            print("text input")
            Kernel.Do_Input = True
        if toggle:
            Kernel.Read_Keyboard()


def CheckHotkey():
    if keyboard.is_pressed("-"):
        print("True")
    running = True


def While_Boot():
    if keyboard.is_pressed("]"):
        Kernel.OpenBootSettings()
