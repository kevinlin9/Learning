def file_write(file_name):
    with open(file_name, "w+") as file:
        print("Writing")
        file.write("I wrote something!")

def file_read(file_name):
    with open(file_name, "r+") as file:
        print("Reading")
        for line in file.readlines():
            print(line)

def file_example(file):
    file_write(file)
    file_read(file)

file = "FileTest.txt"
file_example(file)
