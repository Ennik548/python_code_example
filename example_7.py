# Задача 1
"""
Задача: разработать класс, который представляет собой экземпляр пива.

Функциональные требования:
• Класс должен иметь атрибуты «Название», «Объем» и «IBU», которые должны
 присваиваться инициализатору при создании экземпляра класса;
• Класс должен иметь метод «Сгонять», который возвращает
 строку в зависимости от значения «IBU»:
 - Если «IBU» меньше 10 - «Слабое пиво»;
 - Если «IBU» меньше 30 - «Среднее пиво»;
 - - противном случае - «Крепкое пиво»;
• Класс должен иметь метод «Представление», возвращающий
 строку в виде «название пива (объем)»;
• Класс должен иметь метод «Оценка», возвращающий
 строку в зависимости от значения «IBU»:
 - Если «IBU» меньше 10 - «Очень сладкое пиво»;
 - Если «IBU» меньше 30 - «Отличное пиво»;
 - B противном случае - «Очень горькое пиво»;

Нефункциональные требования:
• Код должен быть простым и читаемым;
• Использовать имена переменных и функций, соответствующие их функциям;
• Использовать правильные практики ООП.
"""


class Beer:
    def __init__(self, name, volume, ibu) -> None:
        self.name = name
        self.volume = volume
        self.ibu = ibu

    def __str__(self) -> str:
        return f"{self.name} ({self.volume})"

    def brew_strength(self):
        if self.ibu < 10:
            return "Слабое пиво"
        elif self.ibu < 30:
            return "Среднее пиво"
        else:
            return "Крепкое пиво"

    def rating(self):
        if self.ibu < 10:
            return "Очень сладкое пиво"
        elif self.ibu < 30:
            return "Отличное пиво"
        else:
            return "Очень горькое пиво"


Tagil = Beer("Тагил Рулит", 0.5, 100)
print(Tagil)

# Задача 2
"""
2) Задача на наследование:
1. Цель
Создание классов для представления сущностей "Барби" и "Кукла Барби" на языке
Python с использованием принципов ООП наследования.

2. Требования
2.1. Необходимо создать два класса: "Барби" (Barbie)
    и "Кукла Барби" (BarbieDoll).
2.2. Класс "Барби" должен содержать информацию
    о внешнем виде, ментальности и характере Барби.
2.3. Класс "Кукла Барби" должен наследовать все свойства класса "Барби"
и также содержать информацию о материале, из которого она сделана
    (пластик, бархат и т.д.), о типе производства (массовое или ограниченное),
    цвете, дополнительных атрибутах и деталях
    (настроечные глаза, тканевые юбки и т.п.).
2.4. Для каждого класса требуется создать методы,
    которые позволят получать и изменять значения атрибутов.

3. Инструкция
3.1. Создайте два класса: "Барби" и "Кукла Барби".
3.2. В класс "Барби" добавьте атрибуты для представления ее внешнего вида,
     ментальности и характера.
3.3. В класс "Кукла Барби" добавьте атрибуты, такие как материал, из которого
    она сделана, тип производства, цвет и дополнительные атрибуты и детали.
3.4. Укажите для каждого класса методы для получения и изменения атрибутов.
3.5. Убедитесь, что класс "Кукла Барби" наследует все атрибуты
    и методы класса "Барби".
"""


class Barbie:
    def __init__(self, appearance, mentality, character) -> None:
        self.appearance = appearance
        self.mentality = mentality
        self.character = character

    def get_appearance(self):
        return self.appearance

    def set_appearance(self, new_appearance):
        self.appearance = new_appearance

    def get_mentality(self):
        return self.mentality

    def set_mentality(self, new_mentality):
        self.mentalityy = new_mentality

    def get_character(self):
        return self.character

    def set_character(self, new_character):
        self.character = new_character


class BarbieDoll(Barbie):
    def __init__(self, material, production_type, color, attributes, details,
                 appearance, mentality, character) -> None:
        super().__init__(appearance, mentality, character)
        self.material = material
        self.production_type = production_type
        self.color = color
        self.attributes = attributes
        self.details = details

    def get_material(self):
        return self.material

    def set_material(self, new_material):
        self.material = new_material

    def get_production_type(self):
        return self.production_type

    def set_production_type(self, new_production_type):
        self.production_type = new_production_type

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_attributes(self):
        return self.attributes

    def set_attributes(self, new_attributes):
        self.attributes = new_attributes

    def get_details(self):
        return self.details

    def set_details(self, new_details):
        self.details = new_details


barbie_doll = BarbieDoll('пластик',
                         'массовое',
                         'цвет кожи',
                         'умеет читать реп',
                         'татуировки на лице как у lil peepa',
                         'гангстер', 'достаточно ментальная', 'веселая')

print(f"{barbie_doll.get_appearance()} {barbie_doll.get_mentality()}"
      f" {barbie_doll.get_character()}")
barbie_doll.set_character("грустная")
print(f"{barbie_doll.get_appearance()} {barbie_doll.get_mentality()}"
      f" {barbie_doll.get_character()}")
