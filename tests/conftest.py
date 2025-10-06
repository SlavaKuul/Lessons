import pytest


@pytest.fixture
def state_and_date_executed() -> list[dict]:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def state_and_date_sort() -> list[dict]:
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-29T02:08:58.425572'}]


@pytest.fixture
def state_and_date_sort_equal() -> list[dict]:
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def state_and_date_sort_format() -> list[dict]:
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': 'today'}]
