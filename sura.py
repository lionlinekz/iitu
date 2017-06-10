# coding=utf-8
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iitu.settings')
import django
django.setup()
from ticket.models import Sura


with open('sureler.json') as data_file:    
    data = json.load(data_file)

key, values = data.popitem()

i = 1
for value in values:
	sura = Sura()
	sura.index = i
	sura.arabic_name = value['FIELD5']
	sura.kazakh_name = value['FIELD6']
	sura.ayat_count = int(value['FIELD2'])
	sura.ayat_start_index = int(value['FIELD1'])
	sura.save()
	i += 1


