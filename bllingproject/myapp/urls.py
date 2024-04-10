from django.urls import path
from.views import registerEmployee,loginEmployee,AddProduct,update_delete_product,ManageCustomer,addcustomer


urlpatterns = [
    path('register/', registerEmployee.as_view(), name='user-registration'),
    path('login/', loginEmployee.as_view(), name='user-login'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('updatedeleteproduct/<int:pk>/',update_delete_product.as_view(), name='updatedeleteproduct'),
    path('addcustomer/', addcustomer.as_view(), name='addcustomer'),
    path('managecustomer/<int:pk>/',ManageCustomer.as_view(), name='managecustomer'),
   
   

]