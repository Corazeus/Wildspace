from django.contrib.auth.views import LoginView
from django.contrib import messages

class UserLoginController(LoginView):
    template_name = 'wil/userlogin.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)




