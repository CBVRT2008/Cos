# load driver script

file = ""
output = ""


def Driver(driver_path):
    global output
    driver = open(driver_path, "r")
    file2 = []
    line_count = 0
    for line in driver:
        if line != "\n":
            line_count += 1
            file2.append(line)
    output = file2
    driver.close()