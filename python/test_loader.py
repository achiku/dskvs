# -*- coding: utf-8 -*-
from .loader import create_data


def test_create_data(file_path):
    d = create_data(file_path)
    assert 6 == len(d.keys())
