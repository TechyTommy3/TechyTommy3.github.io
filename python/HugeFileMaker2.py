name = "Tommy"
print("Welcome to HugeFileMaker 2, " + name + "! What do you want to do?")
print("N - New File")
print("A - Make File Bigger")
option = input("Choose one: ")
if option == "N":
    method = input("What do you want to do? Type 0 to use 0 only, or type 123456789 to use a random number.")
    filepath = input("What's the path of the file to create?")
    sizetype = input("Do you want to use bytes, kilobytes, megabytes, gigabytes, or terabytes?")
    sizesetence = "How many " + sizetype + " do you want the file?"
    size = input(sizesetence)
    print("Making file bigger...")
    file = open(filepath, "a")
    if sizetype == "bytes":
        for x in range(int(size)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "kilobytes":
        kilobytes = int(size) * 1000
        for x in range(int(kilobytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "megabytes":
        megabytes = int(size) * 1048576
        for x in range(int(megabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "gigabytes":
        gigabytes = int(size) * 1073741824
        for x in range(int(gigabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "terabytes":
        terabytes = int(size) * 1099511627776
        for x in range(int(terabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    print("Finished!")
    file.close()
if option == "A":
    print("Making a file bigger is not recommended. Making a file bigger could result in damage of the file. Press Ctrl+C to stop at any time.")
    method = input("What do you want to do? Type 0 to use 0 only, or type 123456789 to use a random number.")
    filepath = input("What's the path of the file to make bigger?")
    sizetype = input("Do you want to use bytes, kilobytes, megabytes, gigabytes, or terabytes?")
    sizesetence = "How many " + sizetype + " do you want the file?"
    size = input(sizesetence)
    print("Making file bigger...")
    file = open(filepath, "a")
    if sizetype == "bytes":
        for x in range(int(size)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "kilobytes":
        kilobytes = int(size) * 1000
        for x in range(int(kilobytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "megabytes":
        megabytes = int(size) * 1048576
        for x in range(int(megabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "gigabytes":
        gigabytes = int(size) * 1073741824
        for x in range(int(gigabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    if sizetype == "terabytes":
        terabytes = int(size) * 1099511627776
        for x in range(int(terabytes)):
            if method == "0":
                file.write("0")
            if method == "123456789":
                randomnumber = random.randint(0, 9)
                file.write(str(randomnumber))
    print("Finished!")
    file.close()
    
