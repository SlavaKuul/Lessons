import masks


def mask_account_card(type_and_number: str) -> str:
    """Функция маски номера карты, а также номера счёта пользователя"""
    input_split = type_and_number.split()
    if len(input_split[-1]) == 16:
        return (f"{' '.join(input_split[:-1])} {masks.get_mask_card_number(input_split[-1])}")
    else:
        return (f"{' '.join(input_split[:-1])} {masks.get_mask_account(input_split[-1])}")


def get_date(date: str) -> str:
    """Функция формата даты"""
    splited_date = date.split(sep='-', maxsplit=4)
    return (f"{splited_date[2][:2]}.{splited_date[1]}.{splited_date[0]}")
