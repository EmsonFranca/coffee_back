from rest_framework import serializers
from register.models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id','name','email','user_name','password','confirm_password']