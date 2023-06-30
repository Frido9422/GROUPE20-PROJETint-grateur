from django.db import models


# Create your models here.

class form_1(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=18)
    number = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    code = models.CharField(max_length=20)
    state = models.CharField(blank=True, max_length=20)

class form_2(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=18)
    state = models.CharField(max_length=20)
    permission = models.CharField(max_length=3)


class form_3(models.Model):
    jour = models.CharField(max_length=8, db_column='jour')
    nom = models.CharField(max_length=100, db_column='nom')
    sept_heure = models.CharField(max_length=2, db_column='sept_heure')
    huit_heure = models.CharField(max_length=2, db_column='huit_heure')
    neuf_heure = models.CharField(max_length=2, db_column='neuf_heure')
    dix_heure = models.CharField(max_length=2, db_column='dix_heure')
    onze_heure = models.CharField(max_length=2, db_column='onze_heure')
    douze_heure = models.CharField(max_length=2, db_column='douze_heure')
    treize_heure = models.CharField(max_length=2, db_column='treize_heure')
    quatorze_heure = models.CharField(max_length=2, db_column='quatorze_heure')
    quinze_heure = models.CharField(max_length=2, db_column='quinze_heure')
    seize_heure = models.CharField(max_length=2, db_column='seize_heure')
    dix_sept_heure = models.CharField(max_length=2, db_column='dix_sept_heure')
    dix_huit_heure = models.CharField(max_length=2, db_column='dix_huit_heure')
    dix_neuf_heure = models.CharField(max_length=2, db_column='dix_neuf_heure')
    dix_neuf_heure = models.CharField(max_length=2, db_column='dix_neuf_heure')

class form_5(models.Model):
    lundi = models.CharField(max_length=1000000, db_column='lundi')
    mardi = models.CharField(max_length=1000000, db_column='mardi')
    mercredi = models.CharField(max_length=1000000, db_column='mercredi')
    jeudi = models.CharField(max_length=1000000, db_column='jeudi')
    vendredi = models.CharField(max_length=1000000, db_column='vendredi')
    samedi = models.CharField(max_length=1000000, db_column='samedi')
    occupate = models.CharField(max_length= 1, db_column="occupate")

class verification0(models.Model):
    jour_choisi = models.CharField(max_length=9, db_column='jour_choisi')

