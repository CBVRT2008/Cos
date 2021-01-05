import os
import sys
from Programs import FileEditor
from Programs import Jan


def RunFile(file):
    try:
        if file == "Programs/FileEditor.py":
            FileEditor.Run()

        if file == "Programs/Jan.py":
            Jan.Run()

    except (RuntimeError, TypeError, NameError):
        print("Couldn't start program")
