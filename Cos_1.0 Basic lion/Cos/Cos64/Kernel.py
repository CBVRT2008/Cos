from Cos.Cos64 import Driver_loader
from Cos.Cos64 import Restart
from Cos.Cos64 import Register
import RunFile
import sys

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
    crashed = True
    crash_information = "No further information given"

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

    main(crashed, crash_information, running)


def main(crashed, crash_information, running):
    while running:
        Kernel(crashed, crash_information, running)


def Kernel(crashed, crash_information, running):
    Read_Keyboard()
    if not running:
        Shutdown()


def Read_Keyboard():
    text = input()
    command = text
    Command_Executer(command)


def Command_Executer(command):
    global running
    disable = False
    Len_Command = len(command)
    if command == "shutdown":
        disable = True
        if input("Do you want to shutdown?(y/n)") == "y":
            print("shutting down the os")
            Shutdown()

    if command == "reload":
        if input("Do you want to reload?(y/n)") == "y":
            print("Reloading the os")
            running = False
            disable = True
            Reload()

    if command == "restart":
        if input("Do you want to restart?(y/n)") == "y":
            print("Restarting the os")
            running = False
            disable = True
            Reboot()

    if command == "clear":
        Clear()
        disable = True

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
        Count += 1


def Reload():
    Restart.restart_os()


def Reboot():
    Restart.restart()


def Shutdown():
    global running
    running = False
    sys.exit("Exit code 0: os has been shut-down")


def Prepare_For_shutdown():
    global running
    running = False


def Run(file):
    RunFile.RunFile(file)
