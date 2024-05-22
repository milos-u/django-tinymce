# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
try:
    from django.urls import reverse
except ImportError:
    # Django < 1.10
    from django.core.urlresolvers import reverse

from tinymce.compressor import gzip_compressor

try:
    import enchant
except ImportError:
    enchant = None


def flatpages_link_list(request):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of links to flatpages.
    """
    from django.contrib.flatpages.models import FlatPage
    link_list = [(page.title, page.url) for page in FlatPage.objects.all()]
    return render_to_link_list(link_list)


def compressor(request):
    """
    Returns a GZip-compressed response.
    """
    return gzip_compressor(request)


def render_to_link_list(link_list):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of links suitable for use wit the TinyMCE external_link_list_url
    configuration option. The link_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef('tinyMCELinkList', link_list)


def render_to_image_list(image_list):
    """
    Returns a HttpResponse whose content is a Javascript file representing a
    list of images suitable for use wit the TinyMCE external_image_list_url
    configuration option. The image_list parameter must be a list of 2-tuples.
    """
    return render_to_js_vardef('tinyMCEImageList', image_list)


def render_to_js_vardef(var_name, var_value):
    output = "var {!s} = {!s};".format(var_name, json.dumps(var_value))
    return HttpResponse(output, content_type='application/x-javascript')


def filebrowser(request):
    try:
        fb_url = request.build_absolute_uri(reverse('fb_browse'))
    except Exception:
        fb_url = request.build_absolute_uri(reverse('filebrowser:fb_browse'))

    return render(
        request,
        'tinymce/filebrowser.js',
        {'fb_url': fb_url},
        content_type='application/javascript'
    )
