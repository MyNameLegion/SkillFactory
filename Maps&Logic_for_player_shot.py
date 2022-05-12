from random import randint

map_1 = [["O"]*8 for z in range(9)]
map_2 = [["O"]*8 for i in range(9)]
map_3 = [["O"]*8 for a in range(9)]
def show():
    print("  | 1 | 2 | 3 | 4 | 5 | 6 |    | 1 | 2 | 3 | 4 | 5 | 6 |")
    for z in range(1,7):
        print(f"{z} | {map_1[z][1]} | {map_1[z][2]} | {map_1[z][3]} | {map_1[z][4]} | {map_1[z][5]}"
              f" | {map_1[z][6]} |"
              f"  {z} | {map_2[z][1]} | {map_2[z][2]} | {map_2[z][3]} | {map_2[z][4]} | {map_2[z][5]}"
              f" | {map_2[z][6]} |")

count_player = 0
count_II = 0
def ask_player_shot():

    while True:


        print("____________МОРСКОЙ БОЙ____________"
            "_________________________________________\n")

        asking = input("Введите координаты X&Y куда стреляем:\n").split()
        global count_player
        if len(asking)!= 2:
            print("Введите 2 числа")
            continue
        x, y = asking

        if not x.isdigit() or not y.isdigit():
            print("Введите цифры")
            continue
        x, y = int(x), int(y)

        if x < 1 or x > 6 or y < 1 or y > 6:
            print("Введите координаты в указанном диапазоне")
        if count_player == 11:
            break
        if map_3[x][y] == "■":
            map_1[x][y] = "X"
            print("Попадание!")
            count_player+=1
            if map_3[x][y-1] != "■" and map_3[x][y+1] != "■" and map_3[x+1][y+1] != "■" and map_3[x+1][y] != "■" \
                and map_3[x+1][y-1] != "■" and map_3[x-1][y-1] != "■" and map_3[x-1][y + 1]!= "■"\
                and map_3[x-1][y]!= "■":
                map_1[x][y - 1] = "•"
                map_1[x][y + 1] = "•"
                map_1[x + 1][y + 1] = "•"
                map_1[x + 1][y] = "•"
                map_1[x + 1][y - 1] = "•"
                map_1[x - 1][y - 1] = "•"
                map_1[x - 1][y + 1] = "•"
                map_1[x - 1][y] = "•"
            show()
            continue
        if map_1[x][y] == "•" or map_1[x][y] == "X":
            print("Вы уже стреляли в эту точку, выберите другие координаты")
            continue

        if map_3[x][y] == "O":
            map_1[x][y] = "•"
            print("Мимо")

        show()
        return x, y

def II_shot():

    while True:
        x = randint(1,6)
        y = randint(1,6)
        global count_II
        if count_II == 11:
            break
        if map_2[x][y] == "■":
            map_2[x][y] = "X"
            count_II +=1
            print(f"Ваш корабль подбили!")
            if map_2[x][y-1] != "■" and map_2[x][y+1] != "■" and map_2[x+1][y+1] != "■" and map_2[x+1][y] != "■" \
                    and map_2[x+1][y-1] != "■" and map_2[x-1][y-1] != "■" and map_2[x-1][y + 1]!= "■"\
                    and map_2[x-1][y]!= "■":
                map_2[x][y - 1] = "•"
                map_2[x][y + 1] = "•"
                map_2[x + 1][y + 1] = "•"
                map_2[x + 1][y] = "•"
                map_2[x + 1][y - 1] = "•"
                map_2[x - 1][y - 1] = "•"
                map_2[x - 1][y + 1] = "•"
                map_2[x - 1][y] = "•"
            continue
        if map_2[x][y] == "•" or map_2[x][y] == "X":
            continue
        if map_2[x][y] == "O":
            map_2[x][y] = "•"
            print("ИИ промахнулся")
        show()
        return x,y

class II_Ship:
    def chooise_ship_3x1(self,):
        while True:
            #задаем случайное значение оси X&Y
            x = randint(1,6)
            y = randint(1,6)
            #если клетка занята кораблем, задаем новое значение
            if map_3[x][y] == "■":
                continue
            #если ось Y у верхнего правого края, задаем направление построения
            if y >= 5 and x<=2:
                #так как имеем 2 вектора потенциального направления построение, создаем вероятность для каждой в 50%
                a = randint(1,10)
                #проверяем чтоб перед построением в нужном векторе, не было кораблей в 2 вектора, правого верхнего угла
                if a >= 5 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y-1] = "■"
                    map_3[x][y-2] = "■"
                elif a <= 5 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x+1][y] = "■"
                    map_3[x+2][y] = "■"
                else:
                    continue
            # если ось Y у нижнего правого края, задаем 2 направление построения
            if y >= 5 and x >= 5:
                a = randint(1, 10)
                if a >= 5 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y - 1] = "■"
                    map_3[x][y - 2] = "■"
                elif a<=5and map_3[x-1][y] != "■" and map_3[x-2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x - 1][y] = "■"
                    map_3[x - 2][y] = "■"
                else:
                    continue

            # если ось Y у нижнего левого края, задаем 2 направление построения
            if y <= 2 and x >= 5:
                a = randint(1, 10)
                if a >= 5 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y + 1] = "■"
                    map_3[x][y + 2] = "■"

                elif a <= 5 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x - 1][y] = "■"
                    map_3[x - 2][y] = "■"
                else:
                    continue

            # если ось Y у верхнего левого края, задаем 2 направление построения
            if y <= 2 and x <= 2:
                a = randint(1, 10)
                if a >= 5 and map_3[x][y + 1] != "■" and map_3[x][y + 2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y + 1] = "■"
                    map_3[x][y + 2] = "■"

                elif a <= 5 and map_3[x + 1][y] != "■" and map_3[x + 2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x + 1][y] = "■"
                    map_3[x + 2][y] = "■"
                else:
                    continue

            # Если ось Y у верхнего центра края, задаем 3 направления построения
            if 2<y<5 and x <= 2:
                a = randint(1,9)
                if a <= 3 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y-1] = "■"
                    map_3[x][y-2] = "■"
                elif 3<a<=6 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y + 1] = "■"
                    map_3[x][y + 2] = "■"
                elif a>6 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x + 1][y] = "■"
                    map_3[x + 2][y] = "■"
                else:
                    continue

            # Если ось Y у правого центра края, задаем 3 направления построения
            if y >= 5 and x>2 and x<5:
                a = randint(1, 9)
                if a <= 3 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x-1][y] = "■"
                    map_3[x-2][y] = "■"
                elif 3 < a <= 6 and map_3[x][y - 1] != "■" and map_3[x][y -2+ 2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y - 1] = "■"
                    map_3[x][y - 2] = "■"
                elif a > 6 and map_3[x + 1][y] != "■" and map_3[x + 2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x + 1][y] = "■"
                    map_3[x + 2][y] = "■"
                else:
                    continue
            # Если ось Y у нижнего центра края, задаем 3 направления построения
            if 2<y<5 and x>=5:
                a = randint(1, 9)
                if a <= 3 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■":
                    map_3[x][y] = "■"
                    map_3[x-1][y] = "■"
                    map_3[x-2][y] = "■"
                elif 3 < a <= 6 and map_3[x][y - 1] != "■" and map_3[x][y - 2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y - 1] = "■"
                    map_3[x][y - 2] = "■"
                elif a > 6 and map_3[x - 1][y] != "■" and map_3[x - 2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x - 1][y] = "■"
                    map_3[x - 2][y] = "■"
                else:
                    continue

            # Если ось Y у левого центра края, задаем 3 направления построения
            if y<=2 and 2<x<5:
                a = randint(1, 9)
                if a <= 3 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y + 1] = "■"
                    map_3[x][y + 2] = "■"
                elif 3 < a <= 6 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x + 1][y] = "■"
                    map_3[x + 2][y] = "■"
                elif a > 6 and map_3[x - 1][y] != "■" and map_3[x - 2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x - 1][y] = "■"
                    map_3[x - 2][y] = "■"
                else:
                    continue

            # Если ось Y в центре, задаем 3 направления построения
            if 5>y>2 and 2<x<5:
                a = randint(1,8)
                if a <= 2 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x-1][y] = "■"
                    map_3[x-2][y] = "■"
                elif 2 < a <= 4 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■":
                    map_3[x][y] = "■"
                    map_3[x + 1][y] = "■"
                    map_3[x + 2][y] = "■"
                elif 4 < a <= 6 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y-1] = "■"
                    map_3[x][y-2] = "■"
                elif 6 < a <= 8 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■":
                    map_3[x][y] = "■"
                    map_3[x][y+1] = "■"
                    map_3[x][y+2] = "■"
                else:
                    continue

            return x, y
    #Создаем логику построения 2х палубных кораблей, по 3 условиям, углы, длины периметра и центр
    def chooise_ship_2x2(self):
        while True:
            #Ловим ошибку(выхода за диапазон при проверке) через try:
            try:
                x = randint(1,6)
                y = randint(1,6)
                if map_3[x][y] == "■":
                    continue
                #Логика левого верхнего угла
                if x == 1 and y == 1:
                    a = randint(1,10)
                    if a <= 5 and map_3[x+1][y] != "■" and map_3[x+2][y]!="■" and map_3[x+2][y+1]!="■" \
                            and map_3[x+1][y+1]!="■" and map_3[x][y+1]!="■" :
                        map_3[x][y] = "■"
                        map_3[x+1][y] = "■"
                    elif a > 5 and map_3[x][y+1] != "■" and map_3[x][y+2]!="■" and map_3[x+1][y]!="■"\
                            and map_3[x+1][y+1]!="■" and map_3[x+1][y+2]!="■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"
                    else:
                        continue
                # Логика правого верхнего угла
                if x == 1 and y == 6:
                    a = randint(1,10)
                    if a <= 5 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■" and map_3[x+2][y-1] != "■"\
                            and map_3[x+1][y-1] != "■" and map_3[x][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x+1][y] = "■"
                    elif a > 5 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x+1][y] != "■"\
                            and map_3[x+1][y-1] != "■" and map_3[x+1][y-2] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    else:
                        continue
                # Логика правого нижнего угла
                if x == 6 and y == 6:
                    a = randint(1,10)
                    if a <= 5 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x][y-1] != "■" \
                        and map_3[x-1][y-1] != "■" and map_3[x-2][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a > 5 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x-1][y-2] != "■"\
                            and map_3[x-1][y-1] != "■" and map_3[x-1][y] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    else:
                        continue
                # Логика левого нижнего угла
                if x == 6 and y == 1:
                    a = randint(1,10)
                    if a <= 5 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x][y+1] != "■"\
                            and map_3[x-1][y+1] != "■" and map_3[x-2][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a > 5 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■" and map_3[x-1][y] != "■"\
                            and map_3[x-1][y+1] != "■" and map_3[x-1][y+2] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"
                    else:
                        continue
                # Логика для левой стороны
                if 5>=x>=2 and y == 1:
                    a = randint(1,3)
                    if a == 1 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x+1][y] != "■"\
                            and map_3[x-1][y+1] != "■" and map_3[x+1][y+1] != "■" and map_3[x][y+1] != "■"\
                            and map_3[x-2][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a == 2 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■" and map_3[x+2][y+1] != "■"\
                            and map_3[x+1][y+1] != "■" and map_3[x][y+1] != "■" and map_3[x-1][y+1] != "■"\
                            and map_3[x-1][y] != "■":
                        map_3[x][y] = "■"
                        map_3[x + 1][y] = "■"
                    elif a == 3 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■" and map_3[x-1][y] != "■"\
                            and map_3[x-1][y+1] != "■" and map_3[x-1][y+2] != "■" and map_3[x+1][y] != "■"\
                            and map_3[x+1][y+1] != "■" and map_3[x+1][y+2] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"
                    else:
                        continue
                # Логика для верхней стороны
                if x == 1 and 5 >= y >= 2:
                    a = randint(1, 3)
                    if a == 1 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■" and map_3[x+2][y-1] != "■"\
                            and map_3[x+2][y+1] != "■" and map_3[x+1][y-1] != "■" and map_3[x+1][y+1] != "■"\
                            and map_3[x][y+1] != "■" and map_3[x][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x+1][y] = "■"
                    elif a == 2 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x+1][y-2] != "■"\
                            and map_3[x+1][y-1] != "■" and map_3[x+1][y] != "■" and map_3[x+1][y+1] != "■"\
                            and map_3[x][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    elif a == 3 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■" and map_3[x+1][y+2] != "■"\
                            and map_3[x+1][y+1] != "■" and map_3[x+1][y] != "■" and map_3[x+1][y-1] != "■"\
                            and map_3[x][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"

                    else:
                        continue
                # Логика для правой стороны
                if 5>=x>=2 and y == 6:
                    a = randint(1,3)
                    if a == 1 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x-2][y-1] != "■"\
                            and map_3[x-1][y-1] != "■" and map_3[x][y-1] != "■" and map_3[x+1][y-1] != "■"\
                            and map_3[x+1][y] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a == 2 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■" and map_3[x+2][y-1] != "■"\
                            and map_3[x+1][y-1] != "■" and map_3[x][y-1] != "■" and map_3[x-1][y-1] != "■"\
                            and map_3[x-1][y] != "■":
                        map_3[x][y] = "■"
                        map_3[x + 1][y] = "■"
                    elif a == 3 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x+1][y-2] != "■"\
                            and map_3[x-1][y-2] != "■" and map_3[x+1][y-1] != "■" and map_3[x-1][y-1] != "■"\
                            and map_3[x+1][y] != "■" and map_3[x-1][y] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    else:
                        continue
                # Логика для нижней стороны
                if x == 6 and 5 >= y >= 2:
                    a = randint(1, 3)
                    if a == 1 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x-2][y+1] != "■"\
                            and map_3[x-2][y-1] != "■" and map_3[x-1][y+1] != "■" and map_3[x-1][y-1] != "■" \
                            and map_3[x][y+1] != "■" and map_3[x][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a == 2 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x-1][y-2] != "■"\
                            and map_3[x-1][y-1] != "■" and map_3[x-1][y] != "■" and map_3[x-1][y+1] != "■"\
                            and map_3[x][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    elif a == 3 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■" and map_3[x-1][y+2] != "■"\
                            and map_3[x-1][y+1] != "■" and map_3[x-1][y] != "■" and map_3[x-1][y-1] != "■"\
                            and map_3[x][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"
                    else:
                        continue
                # Логика для центра
                if 5 >= x >= 2 and 5 >= y >= 2:
                    a = randint(1, 4)
                    if a == 1 and map_3[x-1][y] != "■" and map_3[x-2][y] != "■" and map_3[x-2][y-1] != "■"\
                            and map_3[x-2][y+1] != "■" and map_3[x-1][y+1] != "■" and map_3[x-1][y-1] != "■"\
                            and map_3[x][y+1] != "■" and map_3[x][y-1] != "■" and map_3[x+1][y] != "■"\
                            and map_3[x+1][y-1] != "■" and map_3[x+1][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x-1][y] = "■"
                    elif a == 2 and map_3[x+1][y] != "■" and map_3[x+2][y] != "■" and map_3[x+2][y+1] != "■" \
                            and map_3[x+2][y-1] != "■" and map_3[x+1][y-1] != "■" and map_3[x+1][y+1] != "■"\
                            and map_3[x][y+1] != "■" and map_3[x][y-1] != "■" and map_3[x-1][y] != "■"\
                            and map_3[x-1][y-1] != "■" and map_3[x-1][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x+1][y] = "■"
                    elif a == 3 and map_3[x][y-1] != "■" and map_3[x][y-2] != "■" and map_3[x+1][y-2] != "■" \
                            and map_3[x-1][y-2] != "■" and map_3[x+1][y-1] != "■" and map_3[x-1][y-1] != "■"\
                            and map_3[x+1][y] != "■" and map_3[x-1][y] != "■" and map_3[x+1][y+1] != "■"\
                            and map_3[x][y+1] != "■" and map_3[x-1][y+1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y-1] = "■"
                    elif a == 4 and map_3[x][y+1] != "■" and map_3[x][y+2] != "■" and map_3[x+1][y+2] != "■"\
                            and map_3[x-1][y+2] != "■" and map_3[x-1][y+1] != "■" and map_3[x+1][y+1] != "■"\
                            and map_3[x-1][y] != "■" and map_3[x+1][y] != "■" and map_3[x+1][y-1] != "■"\
                            and map_3[x][y-1] != "■" and map_3[x-1][y-1] != "■":
                        map_3[x][y] = "■"
                        map_3[x][y+1] = "■"
                    else:
                        continue
            except IndexError:
                continue

            return x, y

    def chooise_ship_1x4(self):

        while True:
            try:
                x = randint(1,6)
                y = randint(1,6)
                if map_3[x][y] != "■" and map_3[x+1][y] != "■" and map_3[x+1][y-1] != "■" \
                        and map_3[x+1][y+1] != "■" and map_3[x][y-1] != "■" and map_3[x][y+1] != "■" \
                        and map_3[x-1][y-1] != "■" and map_3[x - 1][y+1] != "■" and map_3[x-1][y] != "■":
                    map_3[x][y] = "■"

                else:
                    continue

            except IndexError:
                continue

            return x,y

class PlayerShip:
    def chooise_ship_3x1(self):

        while True:

            ship_1x3 = input("Введите 6 последовательныx координаты X&Y, 1го коробля на 3 клетки:").split()

            if len(ship_1x3) != 6:
                print("Введите 6 чисел")
                continue
            x, y, z, a, b, c = ship_1x3

            if not x.isdigit() or not y.isdigit():
                print("Введите цифры")
                continue
            x, y, z, a, b, c = int(x), int(y), int(z), int(a), int(b), int(c)

            if map_2[x][y] == "■" and map_2[z][a] == "■" and map_2[b][c] == "■":
                print("На одной из клеток уже есть корабль")
                continue

            if x == z == b:
                if a == y + 1 or a == y - 1:
                    if c == y + 2 or c == y - 2:
                        map_2[x][y] = "■"
                        map_2[z][a] = "■"
                        map_2[b][c] = "■"
                        print("3 палубный корабль построен!")

                    else:
                        print("Введите координаты Y последовательно")
                        continue
                else:
                    print("Введите координаты Y последовательно")
                    continue

            if y == a == c:
                if z == x + 1 or a == x - 1:
                    if b == x + 2 or c == x - 2:
                        map_2[x][y] = "■"
                        map_2[z][a] = "■"
                        map_2[b][c] = "■"
                        print("3 палубный корабль построен!")

                    else:
                        print("Введите координаты Y последовательно")
                        continue
                else:
                    print("Введите координаты Y последовательно")
                    continue

            if x!=z!=b and y!=a!=c:
                print("Координаты построения введены неверно")
                continue


            if x < 1 or x > 6 or y < 1 or y > 6:
                print("Введите координаты в указанном диапазоне")
            show()
            return x,y

    def chooise_ship_2x2(self):

        while True:
            ship_2x2 = input("Введите 4 последовательные координаты X&Y, 1го коробля на 2 клетки:").split()

            if len(ship_2x2) != 4:
                print("Введите 4 числа")
                continue
            x, y, z, a = ship_2x2

            if not x.isdigit() or not y.isdigit():
                print("Введите цифры")
                continue
            x, y, z, a = int(x), int(y), int(z), int(a)

            if map_2[x][y] == "■" or map_2[z][a] == "■":
                print("На одной из клеток уже есть корабль")
                continue
            # При горизонтальном построение
            if x == z:
                if a == y + 1:
                    if map_2[x][y-1] != "■" and map_2[x][a+1] != "■" and map_2[x-1][a+1] != "■" \
                        and map_2[x+1][a+1] != "■" and map_2[x+1][a] != "■" and map_2[x-1][a] != "■"\
                        and map_2[x-1][y] != "■" and map_2[x+1][y] != "■" and map_2[x-1][y-1] != "■"\
                        and map_2[x+1][y-1] != "■":
                            map_2[x][y] = "■"
                            map_2[z][a] = "■"
                            print("2 палубный корабль построен!")
                    else:
                        print("Не стройте корабли по соседству")
                        continue

                elif a == y - 1:
                    if map_2[x][a-1] != "■" and map_2[x][y+1] != "■" and map_2[x-1][a-1] != "■" \
                        and map_2[x-1][a] != "■" and map_2[x-1][y] != "■" and  map_2[x-1][y+1] != "■" \
                        and map_2[x+1][a-1] != "■" and map_2[x+1][a] != "■" and map_2[x+1][y] != "■" \
                        and map_2[x+1][y+1] != "■":
                            map_2[x][y] = "■"
                            map_2[z][a] = "■"
                            print("2 палубный корабль построен!")
                    else:
                        print("Не стройте корабли по соседству")
                        continue
                else:
                    print("Введите координаты Y последовательно")
                    continue

            #При вертикальном построение
            if y == a:
                if z == x - 1:
                    if map_2[x+1][y] != "■" and map_2[z-1][y] != "■" and map_2[z][y-1] != "■" \
                        and map_2[z - 1][y-1] != "■" and map_2[x][y-1] != "■" and map_2[x+1][y-1] != "■"\
                        and map_2[z-1][y+1] != "■" and map_2[z][y+1] != "■" and map_2[x][y+1] != "■" \
                        and map_2[x+1][y+1] != "■":
                            map_2[x][y] = "■"
                            map_2[z][a] = "■"
                            print("2 палубный корабль построен!")
                    else:
                        print("Не стройте корабли по соседству")
                        continue
                elif z == x + 1:
                    if map_2[x-1][y] != "■" and map_2[z+1][y] != "■" and map_2[z+1][y] != "■" \
                        and map_2[x-1][y-1] != "■" and map_2[x][y-1] != "■" and map_2[z][y-1] != "■" \
                        and map_2[z-1][y-1] != "■" and map_2[x-1][y+1] != "■" and map_2[x][y+1] != "■" \
                        and map_2[z + 1][y+1] != "■" and map_2[z][y+1] != "■":
                            map_2[x][y] = "■"
                            map_2[z][a] = "■"
                            print("2 палубный корабль построен!")
                    else:
                        print("Не стройте корабли по соседству")
                        continue
                else:
                    print("Введите координаты Y последовательно")
                    continue

            if x!=z and y!=a:
                print("Координаты построения введены неверно")


            if x < 1 or x > 6 or y <= 1 or y >= 6:
                print("Введите координаты в указанном диапазоне")
            show()
            return x,y

    def chooise_ship_1x4(self):
        while True:
            ship_1x4 = input("Введите 2 последовательные координаты X&Y, 1го коробля на 1 клетку:").split()

            if len(ship_1x4) != 2:
                print("Введите 2 числа")
                continue
            x, y = ship_1x4

            if not x.isdigit() or not y.isdigit():
                print("Введите цифры")
                continue
            x, y = int(x), int(y)

            if x < 1 or x > 6 or y < 1 or y > 6:
                print("Введите координаты в указанном диапазоне")
                continue

            if map_2[x][y] == "■":
                print("Тут уже есть корабль, выберите другую клетку")
                continue

            if map_2[x - 1][y] != "■" and map_2[x + 1][y] != "■" \
                    and map_2[x - 1][y - 1] != "■" and map_2[x][y - 1] != "■" and map_2[x + 1][y - 1] != "■" \
                    and map_2[x - 1][y + 1] != "■" and map_2[x][y + 1] != "■" and map_2[x + 1][y + 1] != "■":
                map_2[x][y] = "■"
                print("Однопалубный корабль построен!")
            else:
                print("Не стройте корабли по соседству")
                continue
            show()
            return x, y

ii_ship = II_Ship()
player_ship = PlayerShip()
#генерируем кораблии ИИ на невидимом map_3 поле
ii_ship.chooise_ship_3x1()
ii_ship.chooise_ship_2x2()
ii_ship.chooise_ship_2x2()
ii_ship.chooise_ship_1x4()
ii_ship.chooise_ship_1x4()
ii_ship.chooise_ship_1x4()
ii_ship.chooise_ship_1x4()
#генерируем корабли игрока
show()
player_ship.chooise_ship_3x1()
player_ship.chooise_ship_2x2()
player_ship.chooise_ship_2x2()
player_ship.chooise_ship_1x4()
player_ship.chooise_ship_1x4()
player_ship.chooise_ship_1x4()
player_ship.chooise_ship_1x4()

count = 0
while True:
    if count_player == 11:
        print("Победа Игрока")
        break
    if count_II == 11:
        print("Победа ИИ")
        break

    if count == 0 or count%2==0:
        ask_player_shot()
        count+=1
    elif count == 1 or count%2 == 1:
        II_shot()
        count+=1





