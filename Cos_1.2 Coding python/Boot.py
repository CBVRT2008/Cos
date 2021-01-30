from Cos.Cos64 import Kernel
from Cos.Cos64 import CrashHandler
from Cos.Cos64 import Hotkey
import time


def Boot():
    DoBoot = open("Cos/Cos64/Settings/Boot.ini", "r")
    DoBootContents = DoBoot.read()
    DoBoot.close()
    if DoBootContents == "Boot=True":
        DoBootFormat = True

    else:
        DoBootFormat = False

    if DoBootFormat:
        print("Press ] to open boot-settings")
        count = 0
        while count != 500:
            Hotkey.While_Boot()
            count += 1
            time.sleep(0.00000001)
        Kernel.Setup()
        Kernel.startup()

    if not DoBootFormat:
        CrashHandler.CrashHandler("Boot_Is_Disabled", True)


Boot()
