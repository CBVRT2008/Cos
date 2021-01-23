from Cos.Cos64 import Kernel
import Boot
import time


def restart():
    Kernel.Clear()
    Kernel.Prepare_For_shutdown()
    Boot.Boot()


def restart_os():
    Kernel.Prepare_For_shutdown()
    time.sleep(1)
    Kernel.startup()
