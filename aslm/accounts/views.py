from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView as _LoginView
from django.contrib.auth.views import LogoutView as _LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from adil.accounts.forms import UserCreationForm
from adil.accounts.forms import AuthenticationForm
from django.urls.base import reverse_lazy
from django.views.generic.base import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login


class SignUp(FormView):

    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('base:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['breadcrumbs'] = [
            {'name': 'SignUp', 'link': '#', 'is_active': True}
        ]
        return context

    def get(self, request, *args, **kwargs):
        """
        Check if user is logged in
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Check if user is logged in
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(self.request, username=username, password=password)

        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


class LoginView(_LoginView):

    template_name = 'accounts/login.html'
    form_class = AuthenticationForm


class LogoutView(LoginRequiredMixin, _LogoutView):

    template_name = 'accounts/login.html'




