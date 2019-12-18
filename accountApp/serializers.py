from rest_framework import serializers

from accountApp.models import Account


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','real_name','idcard_no','login_name','status','create_date','pause_date','close_date']