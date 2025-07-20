def get_mask_card_number(user_card: str) -> str:
    """Функция маски номера карты пользователя"""
    card_mask = ""
    card_mask += user_card[0:4] + " " + user_card[4:6] + "** **** " + user_card[12:16]
    return card_mask


def get_mask_account(user_account: str) -> str:
    """Функция маски номера счёта пользователя"""
    account_mask = ""
    account_mask += "**" + user_account[-4:]
    return account_mask


print(get_mask_account("73654108430135874305"))
print(get_mask_card_number("1234567812345678"))
