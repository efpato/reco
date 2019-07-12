# -*- coding: utf-8 -*-

import pathlib


def get_api_key():
    filename = pathlib.Path(__file__).parent / 'API_KEY'
    with open(filename) as file:
        return file.read().strip()


def get_site_key():
    filename = pathlib.Path(__file__).parent / 'SITE_KEY'
    with open(filename) as file:
        return file.read().strip()
