#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,get_object_or_404
from plucoApp.forms import userForms,UserProfileForm
from plucoApp.models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated():
        registered = True
        try:
            us = UserProfile.objects.get(user=request.user)
        except:
            us = False
            return render(request, 'hijo.html',{'user': us})
    else:
        us = False
    return render(request, 'hijo.html',{'user': us})

def about(request):
    if request.user.is_authenticated():
        registered = True
        try:
            us = UserProfile.objects.get(user=request.user)
        except:
            us = False
            return render(request, 'about.html',{'user': us})
    else:
        us = False
    return render(request, 'about.html',{'user': us})

def contact(request):
      return render(request,'contact.html')

@login_required
def user_profile(request):
    registered = True
    try:
        us = UserProfile.objects.get(user=request.user)
    except:
        us = False
    return render(request,'perfil.html',{'user' : us})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both userForms and UserProfileForm.
        user_form = userForms(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                picture = "anonymous.png"
                profile.picture = picture
            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = userForms()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Cuenta inactiva, cierra sesión automático")
        else:
            # Bad login details were provided. So we can't log the user in.
            # If the user exists, but the password is incorrect, exists = True
            try:
                (User.objects.get(username=username))
                exists = True
            except:
                exists = False
            return render(request,'errorUser.html',{'error': exists})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def user_address(request):
    return render(request,'address.html')
