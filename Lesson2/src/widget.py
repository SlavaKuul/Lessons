import masks

def mask_account_card(type_and_number: str) -> str:
    """Функция маски номера карты или номера счёта пользователя"""
    input_split = type_and_number.split()
    if len(input_split[-1]) == 16:
        return (f"{' '.join(input_split[:-1])} {masks.get_mask_card_number(input_split[-1])}")
    else:
        return (f"{' '.join(input_split[:-1])} {masks.get_mask_account(input_split[-1])}")

print(mask_account_card("Счёт 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
