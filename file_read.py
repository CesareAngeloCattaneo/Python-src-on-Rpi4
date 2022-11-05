import os

if os.path.exists("/home/Cesare-pi4-2/text_file"):
    with open("/home/Cesare-pi4-2/text_file", "r") as f:
        print("the file exists")
        print(f.read())
else:
    print("the file doesn't exists. I create it!")
    with open("/home/Cesare-pi4-2/text_file", "w") as f:
        f.write("prima riga")

if os.path.exists("/home/Cesare-pi4-2/text_file"):
    with open("/home/Cesare-pi4-2/text_file", "r") as f:
        print("the file exists")
        print(f.read())
else:
    print("the file doesn't exists. I create it!")
    with open("/home/Cesare-pi4-2/text_file", "w") as f:
        f.write("prima riga")

with open("/home/Cesare-pi4-2/text_file", "w") as f:
    f.write("nuova riga")

with open("/home/Cesare-pi4-2/text_file", "a") as f:
    f.write("nuova riga")   
    f.write("nuovissima riga")

if os.path.exists("/home/Cesare-pi4-2/text_file"):
    print("the file exists")
    os.remove("/home/Cesare-pi4-2/text_file")

if os.path.exists("/home/Cesare-pi4-2/text_file"):
    print("the file exists")
else:
    print("the file doesn't exists")
