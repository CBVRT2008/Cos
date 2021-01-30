def UpdateRegister(Name, Location, File):
    Temp1 = open("Cos/Cos64/Temp/RunFile.tmp", "w")
    Temp2 = open("Cos/Cos64/Temp/RunFile1.tmp", "w")
    Driver = open("Cos/Cos64/Drivers/RunFile.drv", "r")
    Register_py = open("Cos/Cos64/RunFile.py", "r")
    Register_reg = open("Cos/Cos64/Register.reg", "r")

    Register_reg_Contents = Register_reg.read()
    Register_reg.close()
    Register_reg = open("Cos/Cos64/Register.reg", "w")
    Name = Name
    Register_reg.write(Register_reg_Contents + Name + "\n" + Location + "/" + Name + "\n")
    Register_reg.close()

    Register_py_Contents = []

    Len_Register = 0
    for line in Register_py:
        Register_py_Contents.append(line)
        Len_Register += 1

    Register_py.close()
    Len_Imports = 0
    Imports = ""
    count = 0
    Current_Line = Register_py_Contents[count]
    while count != Len_Register:
        if Current_Line[0:4] == "from":
            if count != 1:
                Imports = Imports + str(Current_Line)
                Len_Imports += 1

        else:
            Temp1.truncate()
            Imports = Imports + "from " + Location + " import " + File
            Temp1.write(Imports)
            break
        Current_Line = Register_py_Contents[count]
        count += 1

    count = Len_Imports + 2
    Len_Runs = 0
    Runs = ""
    Current_Line = Register_py_Contents[Len_Imports + 2]
    while count != Len_Register - 3:
        if Current_Line[0:10] == "        if":
            Runs = Runs + str(Current_Line) + str(Register_py_Contents[count + 1])
            Len_Runs += 1

        else:
            Temp2.truncate()
            Runs = Runs + str('        if file == "' + Location + "/" +  Name + '":\n            ' + File + ".Run()\n")
            Temp2.write(Runs)
            break
        count += 2
        Current_Line = Register_py_Contents[count]

    Temp1.close()
    Temp2.close()

    Register_py = open("Cos/Cos64/RunFile.py", "w")
    Register_py.truncate()

    Len_Driver = 0
    Line_Imports = 0
    Line_Runs = 0
    Driver_Contents = ""
    for line in Driver:
        if line != "\n":
            if Len_Driver == 0:
                Driver_Contents = Driver_Contents + str(Imports) + "\n"

            if line == "%\n":
                Driver_Contents = Driver_Contents + str(Runs)

            else:
                Driver_Contents = Driver_Contents + str(line)
            Len_Driver += 1

    count = 0
    Driver_Contents2 = ""
    while count != Len_Driver:
        Driver_Contents2 = Driver_Contents
        count += 1
    Register_py.write(Driver_Contents2)
    Register_py.close()
    Driver.close()
    print("Successfully added program to register")
