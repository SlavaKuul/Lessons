def filter_by_state(date_list: list[dict[str, any]], state: str = 'EXECUTED') -> list[dict[str, any]]:
    """Функция фильтрации списка по статусу"""
    filtered_list = []
    for current_id in date_list:
        id_state = current_id.get('state')
        if id_state == state:
            filtered_list.append(current_id)
    return filtered_list


def sort_by_date(date_list: list[dict[str, any]], sort_order: str = 'True') -> list[dict[str, any]]:
    """Функция сортировки списка по дате"""
    if sort_order == 'True':
        sorted_list = sorted(date_list, key=lambda x: x['date'], reverse = True)
    else:
        sorted_list = sorted(date_list, key=lambda x: x['date'])
    return sorted_list
