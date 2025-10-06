import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('type_and_number, expected',
                         [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Счет 73654108430135874305', 'Счет **4305'),
                          ('Viva Cuba 7000792289606361', 'Error type'),
                          ('Высчет 73654108430135874305', 'Error type'),
                          (7000792289606361, 'Error input'),
                          ((1, 2), 'Error input')])
def test_widget(type_and_number: str, expected: str) -> None:
    assert mask_account_card(type_and_number) == expected


@pytest.mark.parametrize('date, expected',
                         [("2024-03-11T02:26:18.671407", '11.03.2024'),
                          ('0000-00-00T00:00:00.000000', '00.00.0000'),
                          ("2024-03-11", 'Error: invalid date'),
                          ('', 'Error: invalid date'),
                          (2024311, 'Error type of date'),
                          ([2024, 3, 11], 'Error type of date')])
def test_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
