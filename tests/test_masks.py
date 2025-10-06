import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_number, expected',
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('0000000000000000', '0000 00** **** 0000'),
                          ('1', 'Error card number'),
                          ('', 'Error card number'),
                          (7000792289606361, 'Error card number'),
                          ((1, 2), 'Error card number')])
def test_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('user_account, expected',
                         [('73654108430135874305', '**4305'),
                          ('00000000000000000000', '**0000'),
                          ('1', 'Error user account'),
                          ('', 'Error user account'),
                          (73654108430135874305, 'Error user account'),
                          ([73654108430135874305], 'Error user account')])
def test_account(user_account: str, expected: str) -> None:
    assert get_mask_account(user_account) == expected
