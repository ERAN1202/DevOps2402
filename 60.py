def get_name():
    current_name = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{current_name}\n")
    my_file.close()

def show_name():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(f"hello {name}")

with open("names.txt") as my_file:
    my_file.readlines()

get_name()
show_name()
