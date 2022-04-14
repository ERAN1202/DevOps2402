'''my_file = open("read_my_contents.txt")
a = my_file.readlines()
print(a)
for line in a:
    print(line, end='')

my_file = open("names.txt", "w")
my_file.write("moshe")
my_file.close()

my_file = open("names.txt", "a")
for i in range(100):
    my_file.write("moshe\n")
my_file.close()
'''
def save_input(name):
    for name in range(5):
        name = input("enter your name: ")
        my_file = open("names.txt", "a")
        my_file.write(f"{name}\n")
        my_file.close()

def show_name():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(f"hello {name}")


save_input("Eran")
show_name()
