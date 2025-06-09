from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, ProfileEditForm, CustomPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 👈 این خط باعث لاگین خودکار می‌شه
            messages.success(request, "ثبت‌نام با موفقیت انجام شد و وارد شدید.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
