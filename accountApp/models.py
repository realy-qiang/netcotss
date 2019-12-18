from django.db import models


# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    recommender_id = models.CharField(null=True,max_length=32)
    login_name = models.CharField(max_length=128)
    login_passwd = models.CharField(max_length=128)
    status = models.NullBooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pause_date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True)
    real_name = models.CharField(max_length=128)
    idcard_no = models.CharField(max_length=128)
    birthdate = models.DateField(null=True)
    gender = models.NullBooleanField(null=True)
    occupation = models.CharField(max_length=128, null=True)
    telephone = models.CharField(max_length=64,null=True)
    email = models.CharField(max_length=64,null=True)
    mailaddress = models.CharField(max_length=256,null=True)
    zipcode = models.IntegerField(null=True)
    qq = models.IntegerField(null=True)
    last_login_time = models.DateTimeField(auto_now=True, null=True)
    last_login_ip = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'account'

