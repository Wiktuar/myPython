# сжатие данных
def encode(message):
    encoded_message = ""
    i = 0
 
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message

# восстановление данных
def decode(message):
    decode = ''
    count = ''

    for char in message:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    
    return decode

# чтение закодированной строки из файла
input = open('c:\help\read.txt', 'r')
message = ""
for line in input:
    message += line
input.close()

print(decode(message=))

# кодирование строки и запись в файл

data = "aaabbcccce"

output = open('c:\help\write.txt', 'w')
output.writelines(encode(data))
output.close()


