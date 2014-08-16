# -*- coding: utf-8 -*-
import csv


def create_data(data_file_path):
    result = {}
    with open(data_file_path, 'r') as fh:
        reader = csv.reader(fh, delimiter='\t')
        for row in reader:
            result[row[0]] = row[1:]
    return result
