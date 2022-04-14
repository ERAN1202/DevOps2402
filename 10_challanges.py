import math

def convert_num_degree(D):
    D = int(input("enter a number: "))
    R = D*(math.pi)/180
    return R

print(convert_num_degree(3))

def sort_list(list_1, str):
    if str == "asc":
       return sorted(list_1)
    elif str == "desc":
        return sorted(list_1, reverse=True)


print(sort_list([3, 12, 1, 7, 2 ,11], "desc"))
print(sort_list([3, 12, 1, 7, 2 ,11], "asc"))

def Dec_To_Bin(num):
    if num >= 1 and num <= 1024:
        Dec_To_Bin(num // 2)
    print(num % 2, end='')

Dec_To_Bin(4)

def count_vowels(str_2):
    count = 0
    vowels = set("aeiou")
    for i in str_2:
        if i in vowels:
            count+= 1
    print("\nno. of vowels: ", count)

count_vowels("eran")






