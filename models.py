# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Item(models.Model):
    i_id = models.IntegerField(primary_key=True)
    i_im_id = models.CharField(unique=True, max_length=8)
    i_name = models.CharField(max_length=50)
    i_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'item'


class LibraryMulticol(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    artists = models.TextField(blank=True, null=True)  # This field type is a guess.
    songs = models.TextField(blank=True, null=True)  # This field type is a guess.
    genres = models.TextField(blank=True, null=True)  # This field type is a guess.
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_multicol'


class LibraryMultirow(models.Model):
    album = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'library_multirow'


class LibraryOnerow(models.Model):
    album = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'library_onerow'


class Stock(models.Model):
    w = models.OneToOneField('Warehouse', models.DO_NOTHING, primary_key=True)
    i = models.ForeignKey(Item, models.DO_NOTHING)
    s_qty = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('w', 'i'),)


class Warehouse(models.Model):
    w_id = models.IntegerField(primary_key=True)
    w_name = models.CharField(max_length=50)
    w_street = models.CharField(max_length=50)
    w_city = models.CharField(max_length=50)
    w_country = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'warehouse'
