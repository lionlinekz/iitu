#! /usr/local/bin/python  -*- coding: UTF-8 -*-
import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iitu.settings')
import django
django.setup()
from ticket.models import Word

from django.core import serializers
with open("audiosimple.txt") as f:
     content = f.readlines()
index = 0
words = Word.objects.all()
for word in words:
	word.qazaq_comment = content[index]
	word.save()
	index += 1
# 	aword = Word.objects.get(index_to_quran=index)
# 	aword.eng = word[:-1]
# 	aword.save()
# 	index += 1
#print serializers.serialize("json", Word.objects.all())
#print words[77796].qazaq_comment
data_to_write = serializers.serialize("json", Word.objects.all())
target = open('worddata.txt', 'w')
target.write(data_to_write)