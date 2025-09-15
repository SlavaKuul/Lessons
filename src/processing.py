def filter_by_state(date_list: list, state = 'EXECUTED') -> list:
    """Функция сортировки списка по статусу"""
    sorted_list = []
    for current_id in date_list:
        id_state = current_id.get('state')
        if id_state == state:
            sorted_list.append(current_id)
    return sorted_list
