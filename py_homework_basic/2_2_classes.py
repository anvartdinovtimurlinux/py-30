class Animal:
    stockyard = []

    def __init__(self, name, weight, kind, preffered_food, sound):
        self.name = name
        self.weight = weight
        self.kind = kind
        self.preffered_food = preffered_food
        self.sound = sound
        self.stockyard.append(self)

    def feed(self, food, food_weight):
        if food != self.preffered_food:
            print(f'Фу, какая гадость! {self.name} отказывается это есть')
        else:
            self.weight += food_weight
            print(f'{self.name} с удовольствием поел')

    def make_sound(self):
        print(self.sound)

    def __str__(self):
        return f'{self.kind} {self.name}, вес - {self.weight}'


class AnimalGivingMilk:
    milk_per_day = {
        'корова': 15,
        'коза': 7,
    }

    def give_milk(self):
        milk_weight = self.milk_per_day[self.kind]
        print(f'{self.name} дала {milk_weight} литров молока')
        self.weight -= milk_weight


class AnimalGivingWool:
    wool_per_month = {
        'овца': 4,
    }

    def give_wool(self):
        wool_weight = self.wool_per_month[self.kind]
        print(f'С {self.name} состригли {wool_weight} кг шерсти')
        self.weight -= wool_weight


class AnimalGivingEggs:
    egg_per_week = {
        'курица': 3,
        'утка': 2,
        'гусь': 2,
    }

    def give_eggs(self):
        eggs = self.egg_per_week[self.kind]
        print(f'{self.name} дала {eggs} яиц')


class Cow(Animal, AnimalGivingMilk):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'корова', 'сено', 'Мууууу')


class Goat(Animal, AnimalGivingMilk):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'коза', 'сено', 'Меееее')


class Sheep(Animal, AnimalGivingWool):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'овца', 'трава', 'Бееее>')


class Hen(Animal, AnimalGivingEggs):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'курица', 'пшено', 'Ко-ко-ко')


class Duck(Animal, AnimalGivingEggs):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'утка', 'трава', 'Ква-ква')


class Goose(Animal, AnimalGivingEggs):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'гусь', 'трава', 'Шшшшшшш')


goose1 = Goose('Серый', 4)
goose2 = Goose('Белый', 5)
cow1 = Cow('Манька', 300)
sheep1 = Sheep('Барашек', 50)
sheep2 = Sheep('Кудрявый', 55)
hen1 = Hen('Ко-Ко', 2)
hen2 = Hen('Кукареку', 3)
goat1 = Goat('Рога', 25)
goat2 = Goat('Копыта', 27)
duck1 = Duck('Кряква', 4)


print('Обычный понедельник на ферме')
print('Пойду пересчитаю свою скотину:')

for index, animal in enumerate(Animal.stockyard):
    print(f'{index + 1}) {animal}')

print('\nТеперь покормим её. К сожалению сено и пшено закончились, пустим всех на травку')
for animal in Animal.stockyard:
    animal.feed('трава', animal.weight / 20)


print('\nХотя и сено подоспело!!!')
for animal in Animal.stockyard:
    if animal.preffered_food == 'сено':
        animal.feed('сено', animal.weight / 15)

print('\nСегодня понедельник, а значит пора проверить наших несушек')
for animal in Animal.stockyard:
    if isinstance(animal, AnimalGivingEggs):
        animal.give_eggs()

print('\nУже вечер, сколько вы весите?')
print(f'{sum(animal.weight for animal in Animal.stockyard):.2f} кг')

print('\nА кто самый тяжелый?')
weight, name = max((animal.weight, animal.name) for animal in Animal.stockyard)
print(f'Это же {name} с весом {weight} кг')

print('\nА теперь пожелаем мне спокойной ночи')
for animal in Animal.stockyard:
    animal.make_sound()
