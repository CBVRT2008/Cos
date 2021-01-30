from Cos.Cos64 import Kernel

message = "\nA fatal error has occured in the currently running prosess that caused a kernel panic\n" \
          "This screen has occured to protect your system against further damage caused by the crashed program\n" \
          "The os will be shut-down after the enter key is pressed\n\n" \
          "All unsaved data will be lost!\n\n\n" \
          "Error code:"

Error_Code = "Kernel_Panic"


def CrashHandler(Custom_Errorcode, Enable_Custom_Errorcode):
    if Enable_Custom_Errorcode:
        Kernel.Crash(message, Custom_Errorcode)

    else:
        Kernel.Crash(message, Error_Code)