from django.db import models


# Create your models here.
from TariffApp.models import UserCost
from accountApp.models import Account


class Service(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    s_account = models.ForeignKey(Account)
    unix_host = models.CharField(max_length=32)
    os_username = models.CharField(max_length=64)
    login_passwd = models.CharField(max_length=32)
    status = models.NullBooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pause_date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True)
    s_usercost = models.ForeignKey(UserCost)

    class Meta:
        db_table = 'service'
