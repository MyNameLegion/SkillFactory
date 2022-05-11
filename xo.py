field = [["-"]*3 for i in range(3)]
def show():
    print("   0  1  2")
    for i in range(3):
        print(f"{i}  {field[i][0]}  {field[i][1]}  {field[i][2]}")



def ask():

    while True:

        cords = input("Введите координаты: ").split()

        if len(cords) != 2:
            print("Введите 2 значения")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue
        x, y = int(x), int(y)

        if x<0 or x>2 or y<0 or y>2:
            print("Введите координаты в нужном диапазоне")
            continue

        if field[x][y] != "-":
            print("Клетка занята")
            continue

        return x, y

def win():
    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append(field[i][j])
        if spisok == ["x","x","x"] or spisok == ["o","o","o"]:
            print(f"Победа {field[i][j]}")
            return True

    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append(field[j][i])
        if spisok == ["x","x","x"] or spisok == ["o","o","o"]:
            print(f"Победа {field[j][i]}")
            return True


        spisok = []
        for i in range(3):
            spisok.append(field[i][i])
        if spisok == ["x", "x", "x"] or spisok == ["o", "o", "o"]:
            print(f"Победа {field[i][i]}")
            return True


        spisok = []
        for i in range(3):
            spisok.append(field[i][2-i])
        if spisok == ["x", "x", "x"] or spisok == ["o", "o", "o"]:
            print(f"Победа {field[i][2-i]}")
            return True

step = 0

while True:
    show()
    if step==0 or step%2==0:
        print("ходит Х")
        step +=1
    else:
        print("Ходит О")
        step+=1


    x, y = ask()

    if step==0 or step%2==0:
        field[x][y] = "o"
    else:
        field[x][y] = "x"

    if win():
        show()
        break

    if step == 9:
        print("Ничья")
        break


