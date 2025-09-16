def get_mask_card_number(user_card: str) -> str:
    """Функция маски номера карты пользователя"""
    if isinstance(user_card, str):
        if len(user_card) == 16:
            card_mask = user_card[0:4] + " " + user_card[4:6] + "** **** " + user_card[12:16]
            return card_mask
    return 'Error card number'


print(get_mask_card_number('Visa Platinum 7000792289606361'))

def get_mask_account(user_account: str) -> str:
    """Функция маски номера счёта пользователя"""
    if isinstance(user_account, str):
        if len(user_account) == 20:
            account_mask = ""
            account_mask += "**" + user_account[-4:]
            return account_mask
    return 'Error user account'
