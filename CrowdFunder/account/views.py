from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect,resolve_url
from django.urls import reverse_lazy,reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import generic

from .models import User
from .forms import *
from .tokens import account_activation_token,send_verification_email

class Login(LoginView):
    form_class = LoginForm
    redirect_authenticated_user=True
    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        return reverse('index')

class CreateAccount(generic.CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('success')
    template_name='registration/signup.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_verification_email(self.request,user)
        return redirect(self.success_url)

def Success(request):
    return render(request, 'registration/success.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(reverse('index'))
    else:
        return redirect(reverse('error'))

def ResendMail(request,uname):
    user = User.objects.get(username=uname)
    send_verification_email(request,user)
    return redirect('success')

class ShowProfile(generic.DetailView):
    model = User
    template_name = 'auth/profile.html'
    context_object_name = 'profileuser'

def Logout(request):
    logout(request)
    return redirect('index')

class EditAccount(generic.UpdateView):
    model = User
    form_class = FullUserForm
    success_url = reverse_lazy('home')
    template_name='registration/edit.html'

class DeleteAccount(generic.DeleteView):
    model = User
    success_url = reverse_lazy('home')

