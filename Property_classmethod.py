from string import ascii_letters    #импортируем кирилицу
class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя-"    #Создаем список исключений
    S_RUS_UPPER = S_RUS.upper()                     #Копия списка, заглавными буквами
    def __init__(self, fio, old, ps, weight):       #Инициализируем данные
        self.verify_fio(fio)                        #Перед инициализацией атрибутов, делаем проверку каждого из них
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)


        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod                                    #Определяем classmethod для работы с атрибутами класса
    def verify_fio(cls, fio):
        if type(fio) != str:                        #Проверяем условие на строковый тип данных
            raise TypeError("ФИО должно быть строкой")  #Если тип данных не строковый, генерируем описание ошибки
        f = fio.split()                 #Генерируем условие для проверки, кол-ва данных в ФИО
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER   #Создаем базу с условиями, латинские буквы +
                                                #наша база с русскими буквами + наша база с заглавными русскими буквами
        for s in f:                             #для каждого элемента в f
            if len(s) < 1:                      #если длина элемента в f меньше 1
                raise TypeError("В ФИО должен быть хотя бы 1 символ")
            if len(s.strip(letters)) != 0:      #если при удалении символов ФИО из коллекции letters остаток != 0
                raise TypeError("В ФИО можно использовать только буквенные символы или -")

    @classmethod
    def verify_old(cls, old):   #Условие на проверку возраста
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом от 14 до 120")

    @classmethod
    def verify_weight(cls, w):  #Условие на проверку веса
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    @classmethod
    def verify_ps(cls, ps): #Условие на проверку паспортных данных
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6: #условие на проверку что номер паспорта состоит из 2 групп
                            # чисел, первая группа из 4 вторая из 6, иначе
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit(): #если эллементы в s не равны цифрам, то
                raise TypeError("Серия и номер паспорта должны быть цифрами")

    @property
    def fio(self):              # обозначаем гетер для ФИО через property
        return self.__fio

    @fio.setter                 # обозначаем сетер для ФИО через гетер, связывая их между собой
    def fio(self, fio):         # даем сетеру значение, которое нужно изменять по запросу
        self.verify_fio(fio)    # даем сетеру условие для проверки
        self.__fio = fio        # если проходит через условие, то приватное __fio = новому значению fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

p = Person('Евтушенко Вася Порошенко', 30, '1234 567891', 80.5)
p.old = 100                 #через сетеры меняем значения
p.ps = "4567 123568"
p.weight = 84.4
p                   #вызываем программу