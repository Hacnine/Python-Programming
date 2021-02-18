import os

try:
    file = open('test_text.txt', "rt")
    file2 = open('test_word.docx', 'a+')
    file3 = open('test_word.ppt', 'a+')

    for i in range(1, 5):
        file2.write("This is new line %d\r\n" % (i + i))

    print(file2.read())
    if os.path.exists("test_word.ppt"):
        os.remove("test_word.ppt")
    else:
        print("The file does not exist")
    file.close()
except Exception as e:
    print(e)

else:
    pass