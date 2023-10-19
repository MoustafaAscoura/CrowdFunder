from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect,resolve_url
from django.urls import reverse_lazy,reverse
from django.views import generic

from .models import User
from .forms import FullUserForm,CreateUserForm

class Login(LoginView):
    redirect_authenticated_user=True
    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        return reverse('index')

class CreateAccount(generic.CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy('token_send')
    template_name='registration/signup.html'
    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)

def Success(request):
    return render(request, 'registration/success.html')

def token_send(request):
    return render(request, 'registration/token.html')

def verify(request , auth_token):
    try:
        user = User.objects.filter(auth_token = auth_token).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'registration/error.html')   


def send_mail_after_registration(email,token):
    subject = "Your account needs to be verified"
    message = f'Hi paste your link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)

class ShowProfile(generic.DetailView):
    model = User
    template_name = 'auth/profile.html'
    context_object_name = 'profileuser'


class EditAccount(generic.UpdateView):
    model = User
    form_class = FullUserForm
    success_url = reverse_lazy('home')
    template_name='registration/edit.html'



def Logout(request):
    logout(request)
    return redirect('index')

class DeleteAccount(generic.DeleteView):
    model = User
    success_url = reverse_lazy('home')

