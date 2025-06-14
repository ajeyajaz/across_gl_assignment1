from tkinter.font import names

from django.urls import path
from  .views import signup_view , login_view ,redirect_view , doctor_dashboard, patient_dashboard


urlpatterns = [
    path('',signup_view, name='signup_view'),
    path('login/',login_view,name='login'),

    path('doctor_dashboard/',doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),

    path('redirect/',redirect_view,name='redirect_view')

]

