import json
import csv

# Задание 1
'''
Файл log_100.json:
1) чему равен общий вклад топ-3 всех IP по
количеству посещений? Указать процентом
2) сколько в файле уникальных IP, с которых
на сайт заходили только 1 раз
'''

res = {}
with open("log_100.json") as f:
    data = json.load(f)
    lst = [d.get("ip") for d in data]
    for key in lst:
        res[key] = res.get(key, 0) + 1
    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
    temp = list(res.values())
    print(sum(temp[:3]) / sum(temp))
    print(len(list(key for key, val in res.items() if val == 1)))


# Задание 2
'''
Файл log_full.csv:
5) найти максимально часто встречающийся IP
6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов
7) найти последнюю запись в логах с этим IP и выяснить
какой user-agent был у этой записи
получить словарь:

suspicious_agent = {
    "ip": '...',            # самый частовстречаемый ip в логах
    'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва
    'count': 29427,         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': '...',     # последний user-agent для этого ip
        'timestamp': '...', # последний timestap для этого ip
    }
}
'''
rows = []
last = {}
temp = {}
res = {}
with open("log_full.csv") as f:
    data = csv.reader(f)
    for row in data:
        rows.append(row[1])
        last[row[1]] = {}
        last[row[1]][row[0]] = row[2]
    rows = rows[1:]
    for key in rows:
        temp[key] = temp.get(key, 0) + 1
    temp = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
    temp = {key: val / total for total in (sum(temp.values()),) for key,
            val in temp.items()}
    first_key = next(iter(temp))
    res["ip"] = first_key
    res["fraction"] = temp.get(first_key)
    res["count"] = rows.count(first_key)
    res["last"] = {"agent": list(last[first_key].items())[0][1]}
    res["last"]["timestamp"] = list(last[first_key].items())[0][0]
print(res)
