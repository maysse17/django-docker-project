from django.conf import settings


def get_manufacturer(request):
    """
    Return manufacturer name
    :param request:
    :return:
    """
    return {'manufacturer': settings.MANUFACTURER}


def get_version(request):
    """
    Return version
    :param request:
    :return:
    """
    return {'version': settings.VERSION}


def get_title(request):
    """
    Return version
    :param request:
    :return:
    """
    return {'title': settings.TITLE}
