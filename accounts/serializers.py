from rest_framework import serializers
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #這一行跟下面一行是一樣的意思
        #fields = ('id', 'song', 'singer', 'last_modify_date', 'created')