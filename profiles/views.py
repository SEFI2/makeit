from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from . import forms
from . import models
from django.contrib.auth import authenticate, login, logout
from django.forms.utils import ErrorList

from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def UpdateProfile(request, pk):
    if pk:
        profile = get_object_or_404(models.Profile, pk=pk)
    else:
        profile = models.Profile(author=request.user)

    if profile.user.id != request.user.id:
        return redirect('/blogs/')

    if request.POST:

        form = forms.UpdateProfileForm(request.POST , request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/blogs/')
    else:
        form = forms.UpdateProfileForm(instance=profile)
    return render(request, 'profiles/profile_form.html' , {'form':form , "pagename" : "Update Profile"})

class SignUp(CreateView):
    model = models.Profile
    form_class = forms.SignUpForm
    success_url = '/users'

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['pagename'] = "Sign Up"
        return context

    def post(self, request, *args, **kwargs):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            password = form.cleaned_data['password']
            confirm_passoword = form.cleaned_data['confirm_password']
            all_rules_satisfied = True

            if confirm_passoword != password:
                form.add_error("confirm_password", "Passwords does not match")
                all_rules_satisfied = False



            if User.objects.filter(username=username).exists():
                form.add_error("username" , "User with this username already exists")
                all_rules_satisfied = False

            if all_rules_satisfied:
                User.objects.create_user(username=username, password=password)
                user = authenticate(username = username, password=password)
                login(request, user)
                profile = models.Profile(user=user)
                profile.save()
                return redirect('/users/')
        return render(request, 'profiles/profile_form.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/users/')
            except Exception:

                form.add_error("username" , "username or password is not correct")

    else:
        form = forms.LoginForm()
    return render(request, 'profiles/profile_form.html' , {'form':form , 'pagename':'Login'})

@login_required
def Logout (request):
    logout(request)

    return redirect('/users/')

class AllUsers(ListView):
    queryset = models.Profile.objects.all()
    model = models.Profile
    template_name = 'profiles/allusers.html'


class ShowProfile(DetailView):
    models = models.Profile
    queryset = models.objects.all()
    template_name = 'profiles/user.html'
