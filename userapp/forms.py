from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(
        required=True, 
        label="ایمیل",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}),
        )
    password1 = forms.CharField(
        label="رمز عبور",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control", "placeholder": "رمز عبور"}),
    )
    password2 = forms.CharField(
        label="تأیید رمز عبور",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control", "placeholder": "تأیید رمز عبور"}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_image', 'password1', 'password2')
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'profile_image': 'عکس پروفایل',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # اگر کلاس از قبل تعریف نشده بود، کلاس Bootstrap رو اضافه کن
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing_classes + ' form-control').strip()

            # برای زیبایی می‌تونی placeholder هم اضافه کنی:
            field.widget.attrs['placeholder'] = field.label



