# Create your views here.

from django.views.generic import TemplateView
from django.aslm.base.tasks import show_hello_world
import logging


logger = logging.getLogger("django")


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        logger.info("Printing Hello from Django View")
        show_hello_world.s().apply_async()
        return super().get(*args, **kwargs)
