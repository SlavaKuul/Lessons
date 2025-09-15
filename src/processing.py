def filter_by_state(date_list: list, state = 'EXECUTED') -> list:
    """Функция сортировки списка по статусу"""
    sorted_list = []
    for current_id in date_list:
        id_state = current_id.get('state')
        if id_state == state:
            sorted_list.append(current_id)
    return sorted_list


def sort_by_date(date_list: list, sort_order = 'True') -> list:
    """Функция сортировки списка по дате"""
    if sort_order == 'True':
        sorted_list = sorted(date_list, key=lambda x: x['date'], reverse = True)
    else:
        sorted_list = sorted(date_list, key=lambda x: x['date'])
    return sorted_list

