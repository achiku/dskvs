# -*- coding: utf-8 -*-
import os
import pytest


@pytest.fixture()
def file_path():
    return os.path.join(os.path.dirname(__file__), 'testdata.tsv')
