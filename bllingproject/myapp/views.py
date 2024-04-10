from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import Employeeserializer,productserializer,customerserializer,EmployeeLoginSerializer
from rest_framework.response import Response
from.models import Employee,Product,Customer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from datetime import datetime, timedelta




# Create your views here.

class registerEmployee(APIView):
    permission_classes = []
    authentication_classes=[]
    def post(self,requset):
        serializer=Employeeserializer(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class loginEmployee(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = EmployeeLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = Employee.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=120),
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            "message": "Login successful",
            "token": token
        })
        # response=Response()

        # response.set_cookie(key='jwt',value=token,httponly=True)
        # response.data={
        #     "message":"login success",
        #     'Authentication TOKEN':token

        # }
        # return response


class AddProduct(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def post(self, request):
        serializer = productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Product added successfully')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

class update_delete_product(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = productserializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Product updated successfully')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return Response(status=204)
 
class addcustomer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        serializer = customerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Customer added successfully')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    


class ManageCustomer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = customerserializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Customer updated successfully')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        messages.success(request, 'Customer deleted successfully')
        return Response(status=204)
