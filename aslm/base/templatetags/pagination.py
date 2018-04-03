"""
This software has been developed by ASLM.

Copyright (c) 2018 ASLM, Inc.

COPYRIGHT:
    This file is the property of ASLM.
    It cannot be copied, used, or modified without obtaining
    an authorization from the authors or a mandated
    member of ASLM.
    If such an authorization is provided, any modified version or
    copy of the software must contain this header.

 WARRANTIES:
    This software is made available by the authors in the hope
    that it will be useful, but without any warranty.
    aslm.com is not liable for any consequence related to the
    use of the provided software.
"""
from django import template
from django.conf import settings
from django.core.paginator import Paginator

register = template.Library()

PAGINATION_SETTINGS = getattr(settings, "PAGINATION_SETTINGS", {})

PAGE_RANGE_DISPLAYED = PAGINATION_SETTINGS.get("PAGE_RANGE_DISPLAYED", 4)
MARGIN_PAGES_DISPLAYED = PAGINATION_SETTINGS.get("MARGIN_PAGES_DISPLAYED", 2)


@register.filter(name='page_range')
def page_range(paginator, number):
    """
    Custom tag to overriddes default paginator's  page_range atribute,
    by handleing a number of displayed page numbers & margins
    NB: Taken from django-pure-pagination
    :param paginator: Paginator object
    :param number: current page number
    :return: list of pages numbers
    """
    assert isinstance(paginator, Paginator), 'must be called with Paginator object'

    if paginator.num_pages <= PAGE_RANGE_DISPLAYED:
        return range(1, paginator.num_pages+1)

    result = []
    left_side = PAGE_RANGE_DISPLAYED/2
    right_side = PAGE_RANGE_DISPLAYED - left_side
    if number > paginator.num_pages - PAGE_RANGE_DISPLAYED/2:
        right_side = paginator.num_pages - number
        left_side = PAGE_RANGE_DISPLAYED - right_side
    elif number < PAGE_RANGE_DISPLAYED/2:
        left_side = number
        right_side = PAGE_RANGE_DISPLAYED - left_side
    for page in range(1, paginator.num_pages+1):
        if page <= MARGIN_PAGES_DISPLAYED:
            result.append(page)
            continue
        if page > paginator.num_pages - MARGIN_PAGES_DISPLAYED:
            result.append(page)
            continue
        if number - left_side <= page <= number + right_side:
            result.append(page)
            continue
        if result[-1]:
            result.append(None)

    return result
