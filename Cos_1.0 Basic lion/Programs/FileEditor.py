def Run():
    running = True
    while running:
        File_Name = input('Input file name or "exit" ')

        if File_Name == "exit":
            running = False
            break

        try:
            file = open(File_Name, "r")
            print("Successfully opened file: " + File_Name)

        except IOError:
            print("File doesn't exist: making new one")
            file = open(File_Name, "w")
            file.close()
            file = open(File_Name, "r+")

        except (RuntimeError, TypeError, NameError, LookupError):
            print("Couldn't open file")
            running = False
            break

        File_Contents = []
        File_Length = 0
        for line in file.readlines():
            File_Contents.append(line)
            File_Length += 1

        print("\n")
        print(str(File_Name) + " has " + str(File_Length) + " lines")
        print(File_Contents)
        file.close()
        file = open(File_Name, "w")


        write = True
        while write:
            Add_Line = input("new line or type | to exit ")
            if Add_Line == "|":
                write = False

            else:
                File_Length += 1
                File_Contents.append(Add_Line + "\n")

        count = 0
        file.truncate()
        file.write("")
        while count != File_Length:
            file.write(File_Contents[count][0:-1])
            file.write("\n")
            count += 1

        file.close()