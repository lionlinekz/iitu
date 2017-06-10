#! /usr/local/bin/python  -*- coding: UTF-8 -*-
import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iitu.settings')
import django
django.setup()
from ticket.models import Word
with open("ewbw.txt") as f:
    content = f.readlines()
index = 1
for word in content:
	aword = Word.objects.get(index_to_quran=index)
	aword.eng = word[:-1]
	aword.save()
	index += 1
