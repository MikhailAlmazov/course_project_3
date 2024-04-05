from src.utils import loading_file, filtered_list, sorted_date, changes_dates, get_hide_numb, get_format_sum
import os
from config import ROOT_DIR


def test_loading_file():
    test_path = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert loading_file(test_path) == []
