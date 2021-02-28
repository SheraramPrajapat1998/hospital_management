from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ProfileRegistrationForm
from django.contrib import auth
import sweetify
from django.http import HttpResponse
from django.contrib import messages


def login(request):
    """
    login user
    input: username and password
    """
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) # returns none or user object
            if user is not None:
                if user.is_active:
                    user_profile = Profile.objects.get(user=user)
                    auth.login(request, user)
                    request.session['user'] = user_profile.user.username
                    request.session['uid'] = user_profile.user.pk

                    return redirect('dashboard')
                else:
                    return HttpResponse("Disabled account")
            else:
                messages.error(request, 'Invalid credentials')
                sweetify.error(request, 'Invalid credentials')
                return redirect('login')
        return render(request, 'accounts/login.html')

def dashboard(request):
    context = {
        'user':"sd"
    }
    return render(request, 'accounts/dashboard.html', context)

def register(request):
    user_form = UserRegistrationForm()
    profile_form = ProfileRegistrationForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = ProfileRegistrationForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            cd = profile_form.cleaned_data
            print(cd['user_type'])
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    return render(request, 'accounts/register.html', {'user_form':user_form, 'profile_form':profile_form})

def logout(request):
    """
    logout user
    """
    if request.method == 'POST':
        # cache.clear()
        request.session.flush()
        auth.logout(request)
        return render(request, 'accounts/login.html')
    auth.logout(request)
    return render(request, 'accounts/logged_out.html')

