def add_rashodi(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        rashodi = input("Введите описание расхода и сумму: ")
        file.write(rashodi + "\n")

def show_rashodis(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        rashodis = file.readlines()
        if rashodis:
            print("Ваши расходы:")
            for rashodi in rashodis:
                print(rashodi.strip())
        else:
            print("Расходов нет.")

add_rashodi("rashodi.txt")
add_rashodi("rashodi.txt")
add_rashodi("rashodi.txt")
show_rashodis("rashodi.txt")