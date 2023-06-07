from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, UpdateView

from core.forms import RegistrationForm, ProfileForm


class LoginPageView(LoginView):
    template_name = 'login.html'


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, files=request.FILES)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('LoginPageView')
        else:
            messages.error(request,'invalid inputs!!.Note that all fields are case sensitive')
        return render(request, 'register.html', context)


class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('LoginPageView')

    def post(self, request):
        return redirect('login')



class ProfilePage(View):
    def get(self, request):
        form = RegistrationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'profilepage.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        context = {'form': form, 'profile_form': profile_form}
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'You updated your profile successfully')
        return render(request, 'profilepage.html', context)
