from typing import Any


def filter_by_state(date_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтрации списка по статусу"""
    filtered_list = []
    for current_id in date_list:
        id_state = current_id.get('state')
        if id_state == state:
            filtered_list.append(current_id)
    return filtered_list


def sort_by_date(date_list: list[dict[str, Any]], sort_order: str = 'True') -> list[dict[str, Any]]:
    """Функция сортировки списка по дате"""
    checked_list = []
    for item in date_list:
        if isinstance(item.get('date'), str):
            if len(str(item.get('date'))) == 26:
                checked_list.append(item)
    if sort_order == 'True':
        sorted_list = sorted(checked_list, key=lambda x: x['date'], reverse=True)
    else:
        sorted_list = sorted(checked_list, key=lambda x: x['date'])
    return sorted_list
