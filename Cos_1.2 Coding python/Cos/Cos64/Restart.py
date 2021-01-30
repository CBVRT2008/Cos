from Cos.Cos64 import Kernel
import Boot
import time


def restart():
    try:
        Kernel.Clear()
        Kernel.Prepare_For_shutdown()
        Boot.Boot()

    except AttributeError:
        Kernel.Crash("Second_Restart_Error", True)


def restart_os():
    try:
        Kernel.Prepare_For_shutdown()
        time.sleep(1)
        Kernel.startup()

    except AttributeError:
        Kernel.Crash("Second_Restart_Error", True)
