# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class UserCost(models.Model):
    name = models.CharField(max_length=50)
    base_duration = models.IntegerField(blank=True, null=True)
    base_cost = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    descr = models.CharField(max_length=100)
    creatime = models.DateTimeField(blank=True, null=True)
    startime = models.DateTimeField(blank=True, null=True)
    cost_type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'usercost'


class Cost(models.Model):
    name = models.CharField(max_length=50)
    base_duration = models.IntegerField(blank=True, null=True)
    base_cost = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    descr = models.CharField(max_length=100)


    class Meta:
        db_table = 'cost'