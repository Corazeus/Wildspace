
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class UserLoginController(View):
    template_name = "wil/userlogin.html"  

    def get(self, request):
        
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
        
        
        context = {'form': form, 'error_message': 'Invalid credentials. Please try again.'}
        return render(request, self.template_name, context)

def user_logout(request):
    logout(request)
    return redirect('user_login')





