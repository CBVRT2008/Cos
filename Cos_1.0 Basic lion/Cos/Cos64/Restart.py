from Cos.Cos64 import Kernel
from Cos.Cos64 import Start
import time


def restart():
    Kernel.Clear()
    Kernel.Prepare_For_shutdown()
    Start.Start()


def restart_os():
    time.sleep(1)
    Kernel.startup()
