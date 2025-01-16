from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    national_code = forms.CharField(max_length=10, required=True, label='کد ملی')
    first_name = forms.CharField(max_length=30, required=True, label='نام')
    last_name = forms.CharField(max_length=30, required=True, label='نام خانوادگی')
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True, label='نقش')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'national_code', 'first_name', 'last_name', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'national_code', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')

class CustomAuthenticationForm(AuthenticationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True, label='نقش')

    def confirm_login_allowed(self, user):
        role = self.cleaned_data.get('role')
        if user.role != role:
            raise forms.ValidationError("نقش انتخابی شما نادرست است.", code='invalid_login')
