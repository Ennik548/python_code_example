def read_last(lines: int, file: str):
    """
    Задача 1:
    Напишите функцию
    read_last(lines: int, file: str)
    которая будет открывать определенный файл file
    и возвращать последние lines строк этого файла
    """
    res = ""
    with open(file, "r", encoding="utf-8") as f:
        lst = (list(reversed(f.readlines())))[:lines]
        for i in reversed(range(len(lst))):
            res += lst[i]
    return res.splitlines(keepends=True)


def longest_words(file: str):
    """
    Задача 2
    Документ article.txt содержит следующий текст:

    Мороз и солнце день чудесный
    Еще ты дремлешь друг прелестный
    Пора красавица проснись
    Открой сомкнуты негой взоры
    Навстречу северной Авроры
    Звездою севера явись

    Требуется реализовать функцию
    longest_words(file: str)
    которая возаращает слово список слов, имеющеие
    максимальную длину, если таковых несколько (или список из 1 слова)
    """
    with open(file, "r", encoding="utf-8") as f:
        lst = sorted(f.read().replace("\n", " ").split(), key=len,
                     reverse=True)
        for i in range(1, len(lst)):
            if len(lst[i]) < len(lst[0]):
                return lst[:i]


def get_basket_amount(file: str) -> int:
    """
    Задача 3:
    Имеется текстовый файл prices.txt с информацией о заказе
    из интернет магазина.В нем каждая строка с помощью символа
    табуляции \t разделена на три колонки:
    - наименование товара;
    - количество товара (целое число);
    - цена (в рублях) товара за 1 шт. (целое число).
    Напишите функцию
    get_basket_amount(file: str) -> int
    которая подсчитываюет общую стоимость заказа и возвращает сумму заказа
    """
    res = 0
    with open(file, "r", encoding="utf-8") as f:
        while True:
            lst = f.readline().replace("\n", " ").split()
            if lst == []:
                return res
            else:
                res += int(lst[1]) * int(lst[2])
