def readFile(path):
    data = open(path, 'r')
    for line in data:
        # в строке обрезаем символ переноса строки, который приходит из файла.
        print(line[:len(line) - 1])

    data.close()

