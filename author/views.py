from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from author.models import Profile
from .forms import SigninForm, ProfileForm


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


class ProfileView(TemplateView):
    template_name = "author/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['author'] = User.objects.get(pk=self.kwargs['pk'])
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('landing_page')
    template_name = "author/profileEdit.html"

    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if request.user != profile.user:
            raise PermissionDenied
        else:
            return super(ProfileEditView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileEditView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        return context