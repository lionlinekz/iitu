from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sura(models.Model):
    index = models.IntegerField()
    arabic_name = models.CharField(max_length=30)
    kazakh_name = models.CharField(max_length=39)
    ayat_count = models.IntegerField()
    ayat_start_index = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return str(self.index)+self.kazakh_name

class Ayat(models.Model):
    sura = models.ForeignKey(Sura)
    index_to_quran = models.IntegerField()
    index_to_surah = models.IntegerField()
    kazakh = models.CharField(max_length=700)
    russian = models.CharField(max_length=700)
    eng = models.CharField(max_length=700)
    arab = models.CharField(max_length=700)
    trans = models.CharField(max_length=700)
    completed = models.BooleanField(default=False)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return str(self.sura.index)+":"+str(self.index_to_surah)

class Word(models.Model):
    ayat = models.ForeignKey(Ayat)
    index_to_quran = models.IntegerField()
    index_to_ayat = models.IntegerField()
    arab = models.CharField(max_length=30)
    qazaq = models.CharField(max_length=70)
    qazaq_comment = models.CharField(max_length=70)
    rus = models.CharField(max_length=70)
    eng = models.CharField(max_length=70)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return str(self.ayat.sura.index)+":"+str(self.ayat.index_to_surah)+":"+str(self.index_to_ayat)+self.qazaq
