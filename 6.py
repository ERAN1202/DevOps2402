my_range = list(range(5))
print(my_range)

my_range = list(range(-2, 5, 3))
print(my_range)

for i in range(5):
    print(i)

names = ["yekutiel", "ginat" , "adi","elisaf", "ariel"]
for name in names:
    if name == "elisaf":
        continue
    print(name)
    if name == "adi":
        print("I've found adi , exiting")
        break

else:
    print("loop finished successfully")

for i in range(len(names)):
    #names[i] = "moshe"
   print(names[i])

a = 0
while a < 5:
   print(a)
   a = a + 1
else:
    print("done")


for i in range(5):
    print(i)
else:
    print("done_2")

    