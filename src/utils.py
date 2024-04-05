import json
from datetime import datetime


def loading_file(file_name):
    """Загружает файл из json и возвращает его в виде списка"""
    with open(file_name, "r", encoding="utf-8") as load_file:
        return json.load(load_file)


def filtered_list(load_file):
    """Фильтрует список"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective


# a = check_list(loading_file("operations.json"))
# print(a)

def sorted_date(json_adjective):
    """Сортирует по дате"""
    json_sort = sorted(json_adjective, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort


# b = sorted_date(filtered_list(loading_file("operations.json")))
# print(b)


def changes_dates(date):
    """Изменяет дату в требуемый формат"""
    obj_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(obj_date, '%d.%m.%Y')


# print(changes_dates('2019-09-06T00:48:01.081967'))

def get_hide_numb(number_hide):
    """Возвращает скрытый номер"""
    req = number_hide.split()
    if req[0] == "Счет":
        return "Счет **" + number_hide[-4:]
    else:
        card_name = " ".join(req[:-1])
    # return f"{card_name} {req[:-1][:4][4:6]}** **** {req[-1][-4:]}"
    return card_name + ' ' + req[-1][:4] + ' ' + req[-1][4:6] + '** **** ' + req[-1][-4:]


# print(get_hide_numb("Visa Gold 3654412434951162"))


def get_format_sum(cash):
    """Возвращает количество денег и обозначение валюты"""
    return f'{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}'


print(get_format_sum({
    "id": 736942989,
    "state": "EXECUTED",
    "date": "2019-09-06T00:48:01.081967",
    "operationAmount": {
        "amount": "6357.56",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 3654412434951162",
    "to": "Счет 59986621134048778289"
}))


def get_main(num_operations=5):
    """Основная функция"""
    load_json = loading_file("operations.json")
    filter_ = filtered_list(load_json)
    sort_date = sorted_date(filter_)

    for operation in sort_date:
        if num_operations == 0:
            break
        print(changes_dates(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(get_hide_numb(operation["from"]) + " -> ", end="")
        print(get_hide_numb(operation["to"]))
        print(get_format_sum(operation), "\n")
        num_operations -= 1


print(changes_dates("2018-03-23T10:45:06.972075"))
# get_main()
