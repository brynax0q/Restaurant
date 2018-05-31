# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2018/5/30 下午12:18'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = os.path.join(BASE_DIR, 'static/')

print(url)