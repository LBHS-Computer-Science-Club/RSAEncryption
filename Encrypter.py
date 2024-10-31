message = "hello world!"
ascii = []
key1 = 12 #e
key2 = 123 #n
encrypted = "" #m

for i in range(len(message)):
    ascii.append(ord(message[i]))

for i in ascii:
    if len(str(i)) == 1:
        i = "00" + str(i)
    elif len(str(i)) == 2:
        i = "0" + str(i)

for i in ascii:
    encrypted += str(i)

encrypted = (int(encrypted)**key1)%key2
print(encrypted)
print(ascii)