from django.views.defaults import page_not_found
from django.views.defaults import server_error
from django.views.defaults import permission_denied
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Class view to display dashboard
    """

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        """
        Create context data from kwargs to be passed to template.
        :param kwargs: data to pass to template
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = {'home': {'is_active': True}}
        return context


def handler403(request):
    """
    custom 403 view
    :param request:
    :return:
    """
    return permission_denied(request, Exception(), template_name='base/403.html')


def handler404(request):
    """
    custom 404 view
    :param request:
    :return:
    """
    return page_not_found(request, Exception(), template_name='base/404.html')


def handler500(request):
    """
    Custom 500 view
    :param request:
    :return:
    """
    return server_error(request, template_name='base/500.html')