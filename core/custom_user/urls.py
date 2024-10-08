from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('staff/', StaffList.as_view(), name='staff_list'),
    path('office-staff/', OfficeStaffList.as_view(), name='office_staff_list'),
    path('staff/update/<int:id>/', UpdateStaff.as_view(), name='staff_update'),
    path('client/', ClientInfo.as_view(), name='client_info'),  # POST
    path('client/<int:id>/', ClientInfo.as_view(), name='client_update'),  # PATCH
    path('user/', UserInfo.as_view(), name='user_info'),
]