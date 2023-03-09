import random
from random import randint


# Задание 1
'''
1) Реализация класса "Карточная игра", который будет содержать методы
для создания колоды карт, раздачи карт игрокам, сравнения карт и т.д.
'''


class Cards:
    def __init__(self, num_players=2) -> None:
        self.__deck = self.create_deck(num_players)
        self.num_players = num_players
        self.players = []
        for i in range(num_players):
            self.players.append([])

    def get_num_players(self):
        return self.num_players

    def create_deck(self, num_players):
        strength = [randint(1, 10) for i in range(10)]  # какие-то описания карт
        hp = [randint(1, 10) for i in range(10)]        # я выбрал силу и хп
        deck = list(zip(strength, hp))
        if num_players > 2:                         # будем маштабирвать так
            if num_players % 2 == 1:                # вдруг кто-то захочет
                deck *= (num_players // 2 + 1)      # сыграть
            else:
                deck *= (num_players // 2)
        random.shuffle(deck)
        return deck

    def __cheat_look_deck(self):
        return self.__deck

    def deal_cards(self):
        for i in range(self.num_players):
            for j in range(5):
                self.players[i].append(self.__deck.pop())

    def compare_cards(self):
        lst_strength = []
        lst_hp = []
        for player in self.players:
            player_strength = sum(x for x, y in player)
            player_hp = sum(y for x, y in player)
            lst_strength.append(player_strength)
            lst_hp.append(player_hp)
        largest_strength = max(lst_strength)
        largest_hp = max(lst_hp)
        the_strongest = lst_strength.index(largest_strength)
        the_hpest = lst_hp.index(largest_hp)
        if largest_strength > largest_hp:
            return f"""
Самый сильный игрок под номером {the_strongest + 1} - {largest_strength} ед. силы!!!
Самый толстый игрок под номером {the_hpest + 1} - {largest_hp} ед. здоровья!!!
СМОЖЕТ ЛИ ИГРОК {the_strongest + 1}???
ДАА У НЕГО ПОЛУЧИЛОСЬ
ПОБЕДИЛ ИГРОК {the_strongest + 1}
"""
        elif largest_strength < largest_hp:
            return f"""
Самый сильный игрок под номером {the_strongest + 1} - {largest_strength} ед. силы!!!
Самый толстый игрок под номером {the_hpest + 1} - {largest_hp} ед. здоровья!!!
СМОЖЕТ ЛИ ИГРОК {the_strongest + 1}???
НЕЕЕТ
У игрока {the_strongest + 1} не хватило сил
"""
        else:
            return f"""
Самый сильный игрок под номером {the_strongest + 1} - {largest_strength} ед. силы!!!
Самый толстый игрок под номером {the_hpest + 1} - {largest_hp} ед. здоровья!!!
НИЧЬЯ
ПРОДОЛЖИМ ИГРУ
"""


# Задание 2
'''
2) Реализация класса "Магазин", который будет содержать информацию о
товарах, их ценах, количестве на складе и т.д. и методы для работы с
этой информацией, такие как добавление/удаление товаров, проведение
продаж, поиск товаров по цене и т.д.
'''


class Shop:
    def __init__(self):
        self.products = {}
        self.total_sales = 0

    def add_product(self, product, price, quantity):
        self.products[product] = {
            "price": price,
            "quantity": quantity
        }

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]

    def update_quantity(self, product, quantity):
        if product in self.products:
            self.products[product]["quantity"] = quantity

    def process_sale(self, product, quantity):
        if product in self.products:
            if self.products[product]["quantity"] >= quantity:
                self.total_sales += self.products[product]["price"] * quantity
                self.products[product]["quantity"] -= quantity

    def search_products(self, price=None, quantity=None):
        matching_products = {}
        for product, product_info in self.products.items():
            if price and product_info["price"] == price:
                matching_products[product] = product_info
            elif quantity and product_info["quantity"] == quantity:
                matching_products[product] = product_info
        return matching_products


# Задание 3
'''
3) Реализовать алгоритм Дейкстры для нахождения кратчайшего пути в графе
'''


def dijkstra(graph, start, end):
    # храним расстояния до каждой вершины
    distances = {vertex: float("inf") for vertex in graph}
    # начинаем от стартовой вершины
    distances[start] = 0
    # храним предков каждой вершины
    previous_vertices = {
        vertex: None for vertex in graph
    }

    vertices = list(graph.keys())

    while vertices:
        # выбираем вершину с наименьшим расстоянием
        current_vertex = min(
            vertices, key=lambda vertex: distances[vertex])
        # если это конечная вершина, то завершаем алгоритм
        if current_vertex == end:
            break
        # удаляем выбранную вершину из списка
        vertices.remove(current_vertex)
        # проходимся по соседям текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            # рассчитываем расстояние до соседа
            alternative_route = distances[current_vertex] + weight
            # если найден более короткий путь, то обновляем расстояние
            # и запоминаем предка
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
    # строим кратчайший путь
    path, current_vertex = [], end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    # путь будет перевернутым, поэтому разворачиваем его
    path = path[::-1]
    return path, distances[end]
