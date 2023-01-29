import model
import view
import constants as c

def write1(inputData):
    output = open(c.path1, 'a')
    for data in model.writeInBook1(inputData):
        output.writelines(data + "\n")

    output.writelines("============")
    output.writelines('\n')
    output.close()
    print("Запись успешно добавлена")

def write2(inputData):
     output = open(c.path2, 'a')
     output.writelines(model.writeInBook2(inputData))
     output.writelines('\n')
     output.close()


def start():
    print(c.text)
    command = 0
    while True:
        command = int(input())
        if command == 4: break
        if(command == 1): 
            view.readFile(c.path1)
        if(command == 2): 
            view.readFile(c.path2)
        if(command == 3): 
            inputData = model.inputData()
            write1(inputData)
            write2(inputData)


