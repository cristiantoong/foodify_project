from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    UserChangeForm, 
    PasswordChangeForm
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash #this session we wanted to continue even after we change the password and redirect the user

from recipes.models import Recipe
from accounts.forms import EditProfileForm, PhotoProfileUpload
#from .forms import SignUpForm


# creates user signup form
def signup_view(request):
    if request.method == 'POST':
        #passing data in an instance of UserCreationForm and validate if the data is valid
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save to db
            user = form.save()

            #log user in
            login(request, user)
            return redirect('accounts:profile')
    else: #if request method is GET
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            #log in user
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('recipe_app:recipes')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recipe_app:recipes')




# User Profile
@login_required(login_url="/accounts/login/")
def view_profile(request):
    logged_in_user_posts = Recipe.objects.filter(author=request.user)
    context = {
        'posts': logged_in_user_posts,
    }
    #args = {'user': request.user}
    return render(request, 'accounts/profile.html', context)


# @login_required(login_url="/accounts/login/")
# def view_profile(request, recipe_id):
#     logged_in_user_posts = Recipe.objects.filter(author=request.user)
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     context = {
#         'posts': logged_in_user_posts,
#         'recipe':recipe
#     }
#     #args = {'user': request.user}
#     return render(request, 'accounts/profile.html', context)


@login_required(login_url="/accounts/login/")
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:

        form = EditProfileForm(instance=request.user)
        context = {
            'form': form,
            }
        return render(request, 'accounts/edit_profile.html', context)



# @login_required(login_url="/accounts/login/")
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         photo_upload_form = PhotoProfileUpload(request.POST, request.FILES)
        
#         if form.is_valid() and photo_upload_form.is_valid():
#             form.save()
#             photo_upload_form.save()
#             return redirect('accounts:profile')
#     else:

#         form = EditProfileForm(instance=request.user)
#         photo_upload_form = PhotoProfileUpload(instance=request.user)
#         context = {
#             'form': form,
#             'photo_upload_form': photo_upload_form
#             }
#         return render(request, 'accounts/edit_profile.html', context)




# def upload_file(request):
#     if request.method == 'POST':
#         photo_upload_form = PhotoProfileUpload(request.POST, request.FILES)

#         if photo_upload_form.is_valid():
#             photo_upload_form.save()
#             return redirect('accounts:profile')
#     else:
#         photo_upload_form = PhotoProfileUpload()
#     return render(request, 'accounts/edit_profile.html', {'photo_upload_form': photo_upload_form})




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'accounts/change_password.html', context)