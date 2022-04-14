#Assignment

#1. Write the following code: a = 1/0;

#a = 1/0

#2. Build a corresponding try-except block to
#avoid exception.

try:
    a = 1/0
    print(a)

except BaseException as e:
    print(f"somethind went wrong: {e.args}")
print("finished")


#3. Is the following code legal?

#try :
#    x = 1
#finally :
#    print(``finally``)

'''SyntaxError: invalid character in identifier'''

#4. What exception types can be caught by the
#following handler?
"except SyntaxError"

#5. What is wrong with using the above type of
#exception handler?


#6. What exceptions can be caught by the
#following handlers?
'''the answer is :
#except IOError'''


#7. Create a text file named “words.txt”
#programmatically

#8. Write your name into the file
My_File = open("words.txt", 'r+')
My_File.write("Eran Bar Haim")
My_File.close()
#9. Read your file content and print it

My_File = open("words.txt", 'r')
A = My_File.read()
print(A)
My_File.close()
#10. Write Hebrew content into your text file and

#print its content programmatically.
My_File = open("words.txt", 'w', encoding='utf-8')
content_2 = My_File.write("ערן בר חיים")
print(content_2)
My_File.close()

#Challenge:
#11. Create an image from code (png file) Hint:
#use Pillow

from  PIL import Image

img = Image.new('RGB', (60, 30), color = 'red')
img.save('pil_red.png')


