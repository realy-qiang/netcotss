from django.db import models

# Create your models here.

class Admin_user(models.Model):
    admin_name = models.CharField(max_length=32)
    super_number = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    class Meta:
        db_table = 'admin_user'