from Cos.Cos64 import Driver_loader, RunFile
from Cos.Cos64 import Hotkey
from Cos.Cos64 import ScreenOfDeath
from Cos.Cos64 import CrashHandler
from Cos.Cos64 import AddToRegister
from termcolor import colored
import sys
import time
import os

Do_Input = True
running = True

Path = ""


def Setup():
    global visual_mode, Canvas, Path

    Path = ""

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
    global running, Do_Input, Path
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
        from Cos.Cos64 import Register
        command = command[4:Len_Command]
        output = ""
        Register.Find_In_Register(command, output)
        disable = True

    # if command[0:2] == "cd":
    #    Path = command[3:Len_Command]
    #    try:
    #        os.listdir("." + Path)
    #    except (NotADirectoryError, FileNotFoundError, FileExistsError):
    #        print(colored("could not change directory", "red"))

    #    if Path == "":
    #        Path = "/"
    #    disable = True

    # if command[0:2] == "ls":
    #    ls = ""
    #    if command[0:2] == command:
    #        Path = str("/" + Path)
    #        print(Path)
    #    else:
    #        Path = command[3:Len_Command]
    #        if Path == "./":
    #            Path = ""
    #    try:
    #        ls = os.listdir("." + Path)

    #    except NotADirectoryError:
    #        print(colored("The givin path doesn't lead to a file", "red"))
    #    except (FileExistsError, FileNotFoundError):
    #        print(colored("Could not find folder", "red"))
    #    Ls_Len = len(ls)
    #    Ls_Index = ""
    #    countls = 0
    #    while countls != Ls_Len:
    #        Ls_Index = Ls_Index + str(ls[countls] + "\n")
    #        countls += 1
    #    print(Ls_Index)
    #    disable = True

    #
    # if command[0:5] == "mkdir":
    #    Mkdir_Name = command[6:Len_Command]
    #    try:
    #        os.mkdir(str(Path + Mkdir_Name))
    #        print("Successfully made " + str(Mkdir_Name) + " at " + Path + "!")
    #    except FileNotFoundError:
    #        print("Ilegal path")

    if command == "help" or command == "?":
        try:
            Doc = open("Cos/doc.txt", "r")
            Doc_Contents = Doc.read()
            print(Doc_Contents)
            disable = True
            Doc.close()

        except FileExistsError:
            print("Could not find file")

    if command[0:13] == "addtoregister":
        Name = command[14:Len_Command]
        Location = input("File location ")
        File = input("File to run ")
        print("After adding the os needs to be restarted manual before use")
        addToRegister(Name, Location, File)

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
    print("[1]VisualMode\n"
          "[2]Boot.ini\n"
          "[0]Exit setup\n")
    print("Enter Number or enter to continue\n")
    Number = input()

    if Number == "1":
        file = open("Cos/Cos64/Settings/VisualMode.ini", "r")
        File_Contents = file.read()
        if File_Contents == "VisualMode=False":
            file.close()
            file = open("Cos/Cos64/Settings/VisualMode.ini", "w")
            file.truncate(1)
            file.write("VisualMode=True")
            print("VisualMode=True")
            file.close()
            CloseBootSettings()

        if File_Contents == "VisualMode=True":
            file.close()
            file = open("Cos/Cos64/Settings/VisualMode.ini", "w")
            file.truncate(1)
            file.write("VisualMode=False")
            print("VisualMode=False")
            file.close()
            CloseBootSettings()

        file.close()

    if Number == "2":
        file = open("Cos/Cos64/Settings/Boot.ini", "r")
        File_Contents = file.read()
        if File_Contents == "Boot=False":
            file.close()
            file = open("Cos/Cos64/Settings/Boot.ini", "w")
            file.truncate(1)
            file.write("Boot=True")
            print("Boot=True")
            file.close()
            CloseBootSettings()

        if File_Contents == "Boot=True":
            file.close()
            Yes_No = input("This action makes the os un-bootable!\nDo you want to continue? (y/n)")
            if Yes_No == "y":
                file = open("Cos/Cos64/Settings/Boot.ini", "w")
                file.truncate(1)
                file.write("Boot=False")
                print("Boot=False")
                file.close()
                CloseBootSettings()
            else:
                print("The action was discontinued!")

    if Number == "0":
        print("Continuing boot")
        Reboot()

        file.close()

    CloseBootSettings()


def CloseBootSettings():
    Prepare_For_shutdown()
    Shutdown()


def Reload():
    from Cos.Cos64 import Restart
    try:
        Restart.restart_os()

    except AttributeError:
        CrashHandler.CrashHandler("Second_Reload_Error", True)


def Reboot():
    from Cos.Cos64 import Restart
    try:
        Restart.restart()

    except AttributeError:
        CrashHandler.CrashHandler("Second_Restart_Error", True)


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


def addToRegister(Name, Loctation, File):
    AddToRegister.UpdateRegister(Name, Loctation, File)
