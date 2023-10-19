from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
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
    success_url = reverse_lazy('profile')
    template_name='registration/signup.html'
    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)

class EditAccount(generic.UpdateView):
    model = User
    form_class = FullUserForm
    success_url = reverse_lazy('home')
    template_name='registration/edit.html'

@login_required(login_url='login')
def ShowProfile(request):
    return render(request, 'auth/profile.html')

def Logout(request):
    logout(request)
    return redirect('index')

class DeleteAccount(generic.DeleteView):
    model = User
    success_url = reverse_lazy('home')

