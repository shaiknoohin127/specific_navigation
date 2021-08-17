from django.urls import path
from app.views import *
app_name='app'

urlpatterns=[
    path('app_hai/',app_hai,name='app_hai'),

]