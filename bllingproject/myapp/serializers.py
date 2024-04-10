from rest_framework import serializers
from.models import Employee,Product,Customer


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','email','password']
        
        

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','price']

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','name','email','phone']
        

class EmployeeLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
