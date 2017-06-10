# coding=utf-8
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iitu.settings')
import django
django.setup()
from ticket.models import Sura, Ayat 


with open('russian.json') as data_file:    
    data = json.load(data_file)

key, values = data.popitem()
# m=0
# for i in range(1, 115):
# 	sura = Sura.objects.get(index = i)
# 	for j in range(1, sura.ayat_count+1):
# 		print i, j
# 		a = values[m]
# 		m += 1
# 		ayat = Ayat.objects.get(index_to_quran=m)
# 		ayat.kazakh = a['Kk value']
# 		ayat.trans  = a['Cyr value']
# 		ayat.save()
m=0
for value in values:
	ind = int(value['-index'])
	sura = Sura.objects.get(index=ind)
	ayats = value['aya']
	for ayat in ayats:
		#ayah = Ayat()
		m += 1
		ayah = Ayat.objects.get(index_to_quran=m)
		ayah.russian=ayat['-text']
		ayah.save()
		#print ayat['-text']
		print m, ayah.russian
		#ayah.save()



