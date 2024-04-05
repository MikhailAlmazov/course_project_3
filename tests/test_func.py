from src.utils import loading_file, filtered_list, sorted_date, changes_dates, get_hide_numb, get_format_sum
import os
from config import ROOT_DIR
import pytest

operations = [{"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
              {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
              {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
              {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}]


@pytest.fixture
def operations_fixture():
    return operations


test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')


def test_loading_file():
    assert loading_file(test_path) == []


def test_filtered_list(operations_fixture):
    assert len(filtered_list(operations_fixture)) == 3


def test_sorted_date(operations_fixture):
    assert [i["id"] for i in sorted_date(operations_fixture)] == [3, 2, 4, 1]


def test_changes_dates():
    assert changes_dates("2018-01-01T00:00:00.000000") == "01.01.2018"


def test_get_hide_numb():
    assert get_hide_numb("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert get_hide_numb("Счет 38573816654581789611") == "Счет **9611"
