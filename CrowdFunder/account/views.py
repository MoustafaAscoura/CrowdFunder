from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,resolve_url
from django.urls import reverse_lazy,reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from social_django.models import UserSocialAuth

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
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(self.get_success_url())

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
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
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
    def get_object(self):
        return self.request.user
    
    model = User
    form_class = FullUserForm
    template_name='registration/edit.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        picture = self.request.FILES.get("picture")
        if picture:
            w, h = get_image_dimensions(picture)
            if w > 800 or h > 800:
                form._update_errors(ValidationError("Picture Dimensions must be 800*800 or less"))
                return self.form_invalid(form)
        else:
            picture = self.get_object().picture
            
        user.picture = picture
        user.save()
        return redirect(reverse_lazy('profile', kwargs={'pk': self.object.id}))
        
class DeleteAccount(generic.DeleteView):
    def get_object(self):
        self.is_social_user = UserSocialAuth.objects.filter(user_id=self.request.user.id).exists()
        self.extra_context={'oauth': self.is_social_user}
        return self.request.user

    model = User
    success_url = reverse_lazy('index')
    

    def form_valid(self, form):
        password = self.request.POST.get('password')
        username=self.object.username
        user_cache = authenticate(self.request, username=username, password=password)
        if user_cache is not None or self.is_social_user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        
        form.error = forms.ValidationError("Wrong password! Try again.")
        return self.form_invalid(form)
    