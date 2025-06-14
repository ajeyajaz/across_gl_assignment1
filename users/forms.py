from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name', 'username', 'email',
                  'profile_pic', 'address_line1', 'city', 'state', 'pincode' ,]