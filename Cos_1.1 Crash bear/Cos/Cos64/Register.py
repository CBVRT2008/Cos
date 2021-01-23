from Cos.Cos64 import Kernel


def Find_In_Register(command, output):
    Register = open("Cos./Cos64/Register.reg", "r")
    Register_Contents = []
    Register_Length = 0
    for line in Register.readlines():
        Register_Contents.append(line)
        Register_Length += 1

    output = ""
    count = 0
    while count != Register_Length:
        if Register_Contents[count] == str(command) + "\n":
            output = Register_Contents[count+1][0:-1]
            print(output)
            Kernel.Run(output)
            break
        count += 2
        if count == Register_Length:
            output = "Program location could not be found"
            print(output)
            count = Register_Length
