from Programs import FileEditor
from Programs import Jan
def RunFile(file):
    try:
        if file == "Programs/FileEditor":
            FileEditor.Run()
        if file == "Programs/Jan":
            Jan.Run()
    except (RuntimeError, TypeError, NameError):
        print("Couldn't start program")
