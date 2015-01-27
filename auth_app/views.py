from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
 
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
 
# Create your views here.
 
 
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
 
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
                return render(request, 'auth_app/index.html', {'error': "Your Enabler account is disabled."})
        else:
            # Bad login details were provided. So we can't log the user in.
            return render(request, 'auth_app/index.html', {'error': "Invalid login details supplied."})
 
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'auth_app/index.html')
 
 
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
 
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')