from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm, AccountUpdateForm
from .models import CustomUser
# Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html', {'next': request.GET.get('next')})

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            next = request.GET.get('next')
            login(request, user)
            if next:
                return redirect(next)
            return redirect('users')
        context['has_error'] = True
        return render(request, 'registration/login.html', context)





class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    

class AccountListView(LoginRequiredMixin, View):
    template_name = 'registration/users.html'

    def get(self, request, *args, **kwargs):
        accounts = CustomUser.objects.all()
        return render(request, self.template_name, {'accounts': accounts})
    

class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    

class AccountUpdateView(View):
    template_name = 'registration/profile_update.html'

    def get(self, request, *args, **kwargs):
        account = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        form = AccountUpdateForm(
            initial={
                'username': account.username,
                'first_name': account.first_name,
                'last_name': account.last_name,
                'email': account.email,
                'image': account.image,
            }
        )
        return render(request, self.template_name, {'account': account, 'form': form})

    def post(self, request, *args, **kwargs):
        form = AccountUpdateForm(request.POST, request.FILES)
        account = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        if form.is_valid():
            account.first_name = request.POST.get('first_name')
            account.last_name = request.POST.get('last_name')
            account.email = request.POST.get('email')
            account.image = request.FILES.get('image')
            account.save()
            return redirect('users')
        return render(request, self.template_name, {
            'form': AccountUpdateForm(
                initial={
                    'username': account.username,
                    'first_name': account.first_name,
                    'last_name': account.last_name,
                    'email': account.email,
                    'image': account.image,
                }),
            'account': account})


class AccountDetailView(View):
    template_name = 'registration/profile.html'

    def get(self, request, *args, **kwargs):
        account = get_object_or_404(CustomUser, pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {'account': account})