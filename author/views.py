from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import RedirectView

from .forms import SigninForm

class SigninView(FormView):
    form_class = SigninForm
    success_url = reverse_lazy('landing_page')
    template_name = 'author/signin.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(SigninView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class SignOutView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse_lazy('landing_page')