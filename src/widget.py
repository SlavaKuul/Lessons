import src.masks


def mask_account_card(type_and_number: str) -> str:
    """Функция маски номера карты, а также номера счёта пользователя"""
    if isinstance(type_and_number, str):
        input_split = type_and_number.split()
        if len(input_split[-1]) == 16:
            if (input_split[0] == 'Visa') and (input_split[1] == 'Platinum'):
                return (f"{' '.join(input_split[:-1])} {src.masks.get_mask_card_number(input_split[-1])}")
            return 'Error type'
        if (input_split[0] == 'Счет'):
            return (f"{' '.join(input_split[:-1])} {src.masks.get_mask_account(input_split[-1])}")
        return 'Error type'
    return 'Error input'

def get_date(date: str) -> str:
    """Функция формата даты"""
    if isinstance(date, str):
        if len(date) == 26:
            splited_date = date.split(sep='-', maxsplit=4)
            return (f"{splited_date[2][:2]}.{splited_date[1]}.{splited_date[0]}")
        return 'Error: invalid date'
    return 'Error type of date'