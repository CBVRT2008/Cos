from Cos.Cos64 import Kernel
from termcolor import colored


def ScreenOfDeath(Text, Error_Code):
    print(colored(str(Text), "red"), Error_Code)
    input()
    Kernel.Prepare_For_shutdown()
    Kernel.Shutdown()
