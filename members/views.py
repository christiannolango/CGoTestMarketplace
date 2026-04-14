from unittest import loader
from django.http import HttpResponse


def members(request):
    template = loader.get_template('sample.html')
    return HttpResponse(template.render({}, request))