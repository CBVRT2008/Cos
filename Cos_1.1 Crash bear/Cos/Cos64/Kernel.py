from Cos.Cos64 import Driver_loader
from Cos.Cos64 import Register
from Cos.Cos64 import Hotkey
from Cos.Cos64 import ScreenOfDeath
from Cos.Cos64 import CrashHandler
import RunFile
import sys
import time

Do_Input = True
running = True


def Setup():
    global visual_mode, Canvas

    read_visual_mode_setting = open("Cos/Cos64/Settings/VisualMode.ini", "r")
    visual_mode_read = read_visual_mode_setting.read()
    read_visual_mode_setting.close()

    if visual_mode_read == "VisualMode=True":
        visual_mode = True
        print("starting visual mode")
        from Cos.Cos64 import Canvas
        Canvas.startup()

    elif visual_mode_read == "VisualMode=False":
        visual_mode = False
        print("starting text mode")


def startup():
    global running

    # define crash indicators
    crashed = False
    Crash_Information = "No further information given"

    # define runtime indicators
    running = True
    runtime_errors = []

    # check driver loading
    Driver_loader.Driver("Cos/Cos64/Drivers/check.drv")
    drvcheck2 = Driver_loader.output
    drvcheck_excpected = ['#begin of driver#\n', '#start driver#\n', 'True\n', '#stop driver#\n', '#end of driver#']

    # check for driver loading
    failcounter = 0
    while failcounter != 3:
        if drvcheck2 == drvcheck_excpected:
            print("Succesfully loaded test driver")
            break

        else:
            print("Couldn't load test driver; retrying")
            failcounter += 1

        if failcounter == 3:
            print("Couldn't load test driver; restarting os")
            Reload()
    if visual_mode:
        print("starting visual mode")
        Canvas.startup()

    main(crashed, Crash_Information, running)


def main(crashed, Crash_Information, running):
    while running:
        Kernel(crashed, Crash_Information, running)


def Kernel(crashed, Crash_Information, running):
    Hotkey.SystemHotkeys()
    Hotkey.CheckHotkey()
    if not running:
        Shutdown()
    if Do_Input:
        Read_Keyboard()


def Read_Keyboard():
    text = input()
    command = text
    Command_Executer(command)


def Command_Executer(command):
    global running, Do_Input
    disable = False
    Len_Command = len(command)
    if command == "shutdown":
        disable = True
        if input("Do you want to shutdown?(y/n)") == "y":
            print("shutting down the os")
            Shutdown()

    if command == "reload":
        if input("Do you want to reload?(y/n)") == "y":
            print("Reloading the os\n"
                  "Do not press any key\n"
                  "Continuing in 2 seconds\n")
            time.sleep(2)
            running = False
            disable = True
            Reload()

    if command == "restart":
        if input("Do you want to restart?(y/n)") == "y":
            print("Restarting the os\n"
                  "Do not press any key\n"
                  "Continuing in 2 seconds\n")
            time.sleep(2)
            disable = True
            Reboot()

    if command == "clear":
        Clear()
        disable = True

    if command == "hotkey":
        disable = True
        count = 0
        while count != 500:
            CheckForHotkey()
            count += 1
            time.sleep(0.0000001)

    if command == "exit":
        Do_Input = False
        disable = True
        Hotkey.Toggle()

    if command == "crash":
        disable = True
        CrashHandler.CrashHandler("User_Started_Screen_Of_Death", True)

    if command[0:3] == "run":
        command = command[4:Len_Command]
        output = ""
        Register.Find_In_Register(command, output)
        disable = True

    else:
        if not disable:
            print("invalid syntax")


def Clear():
    for Count in range(0, 200):
        print("\n")


def CheckForHotkey():
    Hotkey.CheckHotkey()


def OpenBootSettings():
    print("64bit-time: " + str(time.time()))
    print("Clock time: " + str(time.asctime()))
    print("Opened boot setting sucsessfully\n")
    print("[1]VisualMode"
          "[2]Boot.ini")
    print("Press enter to continue")
    input()
    Prepare_For_shutdown()
    Shutdown()


def CloseBootSettings():
    Clear()
    Reboot()


def Reload():
    from Cos.Cos64 import Restart
    Restart.restart_os()


def Reboot():
    from Cos.Cos64 import Restart
    Restart.restart()


def Shutdown():
    global running
    running = False
    sys.exit("Exit code 0: os has been shut-down")


def Prepare_For_shutdown():
    global running
    running = False


def Crash(Crash_Information, Error_Code):
    running = False
    crashed = True
    ScreenOfDeath.ScreenOfDeath(Crash_Information, Error_Code)


def Run(file):
    RunFile.RunFile(file)
