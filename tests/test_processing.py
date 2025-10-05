import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    'state, expected',
    [
        (
            'EXECUTED',
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        ),
        (
            'CANCELED',
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        ),
        (
            'CANCELED',
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        ),
        (
            'NOT_EXECUTED', []
        )
    ]
)
def test_filter_executed(state_and_date_executed: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(state_and_date_executed, state) == expected


@pytest.mark.parametrize(
    'sort_order, expected',
    [
        (
            'True',
            [
                {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-29T02:08:58.425572'}
            ]
        ),
        (
            'False',
            [
                {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-29T02:08:58.425572'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
            ]
        ),
        (
            'Nothing',
            [
                {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-29T02:08:58.425572'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
            ]
        )
    ]
)
def test_sorting(state_and_date_sort: list[dict], sort_order: str, expected: list[dict]) -> None:
    assert sort_by_date(state_and_date_sort, sort_order) == expected


@pytest.mark.parametrize(
    'sort_order, expected',
    [
        (
            'True',
            [
                {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        )
    ]
)
def test_sorting_equal(state_and_date_sort_equal: list[dict], sort_order: str, expected: list[dict]) -> None:
    assert sort_by_date(state_and_date_sort_equal, sort_order) == expected


@pytest.mark.parametrize(
    'sort_order, expected',
    [
        (
            'True',
            [
                {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-11-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        )
    ]
)
def test_sorting_format(state_and_date_sort_format: list[dict], sort_order: str, expected: list[dict]) -> None:
    assert sort_by_date(state_and_date_sort_format, sort_order) == expected
